# -*- coding:utf-8 _*-
""" 
LIB-SSE CODE
@author: Jeza Chen
@license: GPL-3.0 License 
@file: test_CJJ14_PiBas.py
@time: 2022/03/09
@contact: jeza@vip.qq.com
@site:  
@software: PyCharm 
@description: 
"""
import unittest
import sys
sys.path[0] = sys.path[0] + "/../.."
# print(sys.path)

import schemes
import schemes.CJJ14.PiBas.config
from schemes.CJJ14.PiBas.config import PiBasConfig
from schemes.CJJ14.PiBas.construction import PiBas
from schemes.CJJ14.PiBas.structures import PiBasKey, PiBasToken, PiBasEncryptedDatabase, PiBasResult
from test.tools.faker import fake_db_for_inverted_index_based_sse

TEST_KEYWORD_SIZE = 16
TEST_FILE_ID_SIZE = 4

class TestPiBas(unittest.TestCase):

    def test_method_correctness_simple_version(self):
        db = {
            b"China": [b"12345678", b"23221233", b"23421232"],
            b"Ukraine":
                [b"\x00\x00az\x02\x03sc", b"\x00\x00\x00\x00\x01\x00\x02\x01", b"12345678"]
        }

        config_dict = schemes.CJJ14.PiBas.config.DEFAULT_CONFIG

        scheme = PiBas(config_dict)
        key = scheme._Gen()

        encrypted_index, mitra_counters = scheme._Enc(key, db)
        
        scheme._Add(encrypted_index, key, mitra_counters, b"Africa", b"5318008")
        
        token = scheme._Trap(key, b"Africa")
        result = scheme._Search(encrypted_index, token)
        # print(db[b"China"])
        print(result.result)
        # self.assertEqual(db[b"China"].sort(), result.result.sort())
    
    def test_doc(self):
        doc_names = {"shrek-script-pdf.pdf", "shrek-2-script-pdf.pdf"}
        
        config_dict = schemes.CJJ14.PiBas.config.DEFAULT_CONFIG

        scheme = PiBas(config_dict)
        key = scheme._Gen()
        
        encrypted_index = scheme._DocEnc(key, doc_names)
        keyword = input("Enter the keyword you are looking for: ")
        token = scheme._Trap(key, bytes(keyword, 'utf-8'))
        result = scheme._Search(encrypted_index, token)
        print(result.result)
        

    def test_method_correctness(self):
        keyword_count = 1000

        config_dict = schemes.CJJ14.PiBas.config.DEFAULT_CONFIG

        db = fake_db_for_inverted_index_based_sse(TEST_KEYWORD_SIZE,
                                                  TEST_FILE_ID_SIZE,
                                                  keyword_count,
                                                  db_w_size_range=(1, 200))

        scheme = PiBas(config_dict)
        key = scheme._Gen()

        encrypted_index = scheme._Enc(key, db)
        for keyword in db:
            token = scheme._Trap(key, keyword)
            result = scheme._Search(encrypted_index, token)
            self.assertEqual(db[keyword], result.result)

    def test_interface_correctness(self):
        keyword_count = 1000

        config_dict = schemes.CJJ14.PiBas.config.DEFAULT_CONFIG

        db = fake_db_for_inverted_index_based_sse(TEST_KEYWORD_SIZE,
                                                  TEST_FILE_ID_SIZE,
                                                  keyword_count,
                                                  db_w_size_range=(1, 200))

        scheme = PiBas(config_dict)
        key = scheme.KeyGen()
        encrypted_index = scheme.EDBSetup(key, db)
        for keyword in db:
            token = scheme.TokenGen(key, keyword)
            result = scheme.Search(encrypted_index, token)
            self.assertEqual(db[keyword], result.result)

    def test_module_loader(self):
        loader = schemes.load_sse_module("CJJ14.PiBas")
        self.assertEqual(loader.SSEScheme, PiBas)
        self.assertEqual(loader.SSEConfig, PiBasConfig)
        self.assertEqual(loader.SSEKey, PiBasKey)
        self.assertEqual(loader.SSEToken, PiBasToken)
        self.assertEqual(loader.SSEEncryptedDatabase, PiBasEncryptedDatabase)
        self.assertEqual(loader.SSEResult, PiBasResult)

    def test_structure_serialization(self):
        keyword_count = 10

        config_dict = schemes.CJJ14.PiBas.config.DEFAULT_CONFIG

        db = fake_db_for_inverted_index_based_sse(TEST_KEYWORD_SIZE,
                                                  TEST_FILE_ID_SIZE,
                                                  keyword_count,
                                                  db_w_size_range=(1, 200))

        scheme = PiBas(config_dict)
        key = scheme.KeyGen()
        self.assertEqual(key, PiBasKey.deserialize(key.serialize(), scheme.config))

        encrypted_index = scheme.EDBSetup(key, db)
        self.assertEqual(encrypted_index,
                         PiBasEncryptedDatabase.deserialize(encrypted_index.serialize(), scheme.config))

        for keyword in db:
            token = scheme.TokenGen(key, keyword)
            self.assertEqual(token,
                             PiBasToken.deserialize(token.serialize(),
                                                    scheme.config))
            result = scheme.Search(encrypted_index, token)
            self.assertEqual(result,
                             PiBasResult.deserialize(result.serialize(),
                                                     scheme.config))

            self.assertEqual(db[keyword], result.result)

if __name__ == "__main__":
    test = TestPiBas()
    try:
        test.test_method_correctness_simple_version()
    except AssertionError:
        print("It didn't work! :(")
    
