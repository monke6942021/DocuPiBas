# -*- coding:utf-8 _*-
""" 
LIB-SSE CODE
@author: Jeza Chen
@license: GPL-3.0 License 
@file: construction.py 
@time: 2022/03/11
@contact: jeza@vip.qq.com
@site:  
@software: PyCharm 
@description: ΠBas Construction described by Cash et al. [CJJ+14]
"""
import os
import PyPDF2
import re

import schemes.interface.inverted_index_sse
from schemes.CJJ14.PiBas.config import DEFAULT_CONFIG, PiBasConfig
from schemes.CJJ14.PiBas.structures import PiBasKey, PiBasToken, PiBasEncryptedDatabase, PiBasResult
from toolkit.bytes_utils import int_to_bytes


class PiBas(schemes.interface.inverted_index_sse.InvertedIndexSSE):
    """PiBas Construction described by Cash et al. [CJJ+14]"""

    def __init__(self, config: dict = DEFAULT_CONFIG):
        super(PiBas, self).__init__()
        self.config = PiBasConfig(config)
        pass

    def _Gen(self) -> PiBasKey:
        """
        Generate Key
        K2 is not used here now.
        """
        K = os.urandom(self.config.param_lambda)
        return PiBasKey(K)

    def _Enc(self, K: PiBasKey, database: dict) -> tuple[PiBasEncryptedDatabase, dict]:
        """Encrypted the given database under the key"""
        K = K.K
        L = []
        
        mitra_counters = {}

        for keyword in database:
            K1 = self.config.prf_f(K, b'\x01' + keyword)
            K2 = self.config.prf_f(K, b'\x02' + keyword)
            mitra_counters[keyword] = [0]
            for c, identifier in enumerate(database[keyword]):
                l = self.config.prf_f(K1, int_to_bytes(c))
                # print(type(l))
                # print(identifier)
                mitra_counters[keyword] = c
                d = self.config.ske.Encrypt(K2, identifier)
                L.append((l, d))
        return PiBasEncryptedDatabase.build_from_list(L), mitra_counters
    
    def _DocEnc(self, K: PiBasKey, doc_names: list) -> PiBasEncryptedDatabase:
        """Inverted index for a list of document names, to be encrypted."""
        database = {}
        
        for doc_name in doc_names:
            pdfFileObj = open(doc_name, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            
            for i in range(len(pdfReader.pages)):
                pageObj = pdfReader.pages[i]
                word_list = pageObj.extract_text().replace('/', ' ').replace('\n', ' ').replace('.', ' ').replace('!', ' ').replace(',', ' ').replace('?', ' ').replace('(', ' ').replace(')', ' ').split(' ')
                
                for word in word_list:
                    if word.lower() in {'the', 'a', 'an', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                        continue
                    
                    b_word = bytes(word, 'utf-8')
                    
                    if b_word not in database.keys():
                        database[b_word] = {b''}
                        database[b_word].remove(b'')
                    
                    database[b_word].add(bytes(doc_name, 'utf-8'))
                    # print(type(bytes(word, 'utf-8')), type(bytes(doc_name, 'utf-8')))
            
            pdfFileObj.close()
        return self._Enc(K, database)
    
    def _Add(self, edb: PiBasEncryptedDatabase, K: PiBasKey, mitra_counters: dict, keyword: bytes, value: bytes):
        K = K.K 
        
        K1 = self.config.prf_f(K, b'\x01' + keyword)
        K2 = self.config.prf_f(K, b'\x02' + keyword)
        
        if keyword not in mitra_counters.keys():
            mitra_counters[keyword] = 0
        else:
            mitra_counters[keyword] += 1
        
        l = self.config.prf_f(K1, int_to_bytes(mitra_counters[keyword]))
        d = self.config.ske.Encrypt(K2, value)
        
        edb.add(l, d)
        

    def _Trap(self, K: PiBasKey, keyword: bytes) -> PiBasToken:
        """Trapdoor Generation Algorithm"""
        K = K.K
        K1 = self.config.prf_f(K, b'\x01' + keyword)
        K2 = self.config.prf_f(K, b'\x02' + keyword)
        return PiBasToken(K1, K2)

    def _Search(self, edb: PiBasEncryptedDatabase, tk: PiBasToken) -> PiBasResult:
        """Search Algorithm"""
        D = edb.D
        K1, K2 = tk.K1, tk.K2
        result = []
        c = 0
        while True:
            addr = self.config.prf_f(K1, int_to_bytes(c))
            cipher = D.get(addr)
            if cipher is None:
                break
            result.append(self.config.ske.Decrypt(K2, cipher))
            c += 1

        return PiBasResult(result)
    
    # This is untested
    def _OrSearch(self, edb: PiBasEncryptedDatabase, tk1: PiBasToken, tk2: PiBasToken) -> PiBasResult:
        """Search Algorithm"""
        D = edb.D
        K11, K12 = tk1.K1, tk1.K2
        K21, K22 = tk2.K1, tk2.K2
        result = []
        c = 0
        while True:
            addr1 = self.config.prf_f(K11, int_to_bytes(c))
            addr2 = self.config.prf_f(K21, int_to_bytes(c))
            cipher1 = D.get(addr1)
            cipher2 = D.get(addr2)
            if cipher1 is None and cipher2 is None:
                break
            if cipher1 is not None:
                result.append(self.config.ske.Decrypt(K12, cipher1))
            if cipher2 is not None:
                result.append(self.config.ske.Decrypt(K22, cipher2))
            c += 1

        return PiBasResult(list(set(result)))
    
    # This is also untested
    def _AndSearch(self, edb: PiBasEncryptedDatabase, tk1: PiBasToken, tk2: PiBasToken) -> PiBasResult:
        """Search Algorithm"""
        D = edb.D
        K11, K12 = tk1.K1, tk1.K2
        K21, K22 = tk2.K1, tk2.K2
        result1 = []
        result2 = []
        c = 0
        while True:
            addr1 = self.config.prf_f(K11, int_to_bytes(c))
            addr2 = self.config.prf_f(K21, int_to_bytes(c))
            cipher1 = D.get(addr1)
            cipher2 = D.get(addr2)
            if cipher1 is None and cipher2 is None:
                break
            if cipher1 is not None:
                result1.append(self.config.ske.Decrypt(K12, cipher1))
            if cipher2 is not None:
                result2.append(self.config.ske.Decrypt(K22, cipher2))
            c += 1

        result = list(set(result1).intersection(set(result2)))
        
        return PiBasResult(result)

    def KeyGen(self) -> PiBasKey:
        key = self._Gen()
        return key

    def EDBSetup(self,
                 key: PiBasKey,
                 database: dict
                 ) -> PiBasEncryptedDatabase:
        return self._Enc(key, database)

    def TokenGen(self, key: PiBasKey, keyword: bytes) -> PiBasToken:
        return self._Trap(key, keyword)

    def Search(self,
               edb: PiBasEncryptedDatabase,
               token: PiBasToken) -> PiBasResult:
        return self._Search(edb, token)
