import sys
sys.path[0] = sys.path[0] + "/../.."
# print(sys.path)

import schemes
import schemes.CJJ14.PiBas.config
from schemes.CJJ14.PiBas.config import PiBasConfig
from schemes.CJJ14.PiBas.construction import PiBas
from schemes.CJJ14.PiBas.structures import PiBasKey, PiBasToken, PiBasEncryptedDatabase, PiBasResult

config_dict = schemes.CJJ14.PiBas.config.DEFAULT_CONFIG

class Gun:
    def __init__(self, serial_number: str, model: str):
        self.serial_number = bytes(serial_number, "utf-8")
        self.model = bytes(model, "utf-8")

class Owner:
    def __init__(self, first_name: str, last_name: str, reg_num: str, phone_number: str):
        self.first_name = bytes(first_name, "utf-8")
        self.last_name = bytes(last_name, "utf-8")
        self.reg_num = bytes(reg_num, "utf-8")
        self.phone_number = bytes(phone_number, "utf-8")
    
    def serialize_gun(self, gun: Gun) -> bytes:
        serialized_bytes = b"Name: " + self.first_name + b" " + self.last_name + b"\x0a Registration Number: " + self.reg_num + b"\x0a Phone Number: " + self.phone_number + b"\x0a Gun Model: " + gun.model + b"\x0a "
        return serialized_bytes

class County:
    def __init__(self):
        self.scheme = PiBas(config_dict)
        self.key = self.scheme._Gen()
        self.edb, self.counters = self.scheme._Enc(self.key, {})
    
    def search(self, serial_number: bytes):
        token = self.scheme.TokenGen(self.key, serial_number)
        return self.scheme._Search(self.edb, token)
    
    def insert(self, owner: Owner, gun: Gun):
        self.scheme._Insert(self.edb, self.key, self.counters, gun.serial_number, owner.serialize_gun(gun))
    
    def delete(self, owner: Owner, gun: Gun):
        self.scheme._Delete(self.edb, self.key, self.counters, gun.serial_number, owner.serialize_gun(gun))

class State:
    def __init__(self, county_count: int):
        self.scheme = PiBas(config_dict)
        self.key = self.scheme._Gen()
        self.edb, self.counters = self.scheme._Enc(self.key, {})
        self.counties = []
        for i in range(county_count):
            self.counties.append(County())
            
    def search(self, serial_number: bytes):
        token = self.scheme.TokenGen(self.key, serial_number)
        return self.scheme._Search(self.edb, token)
    
    def search_county(self, serial_number: bytes, county_idx: int):
        return self.counties[county_idx].search(serial_number)
    
    def insert(self, county_idx: int, owner: Owner, gun: Gun):
        self.scheme._Insert(self.edb, self.key, self.counters, gun.serial_number, bytes(str(county_idx), "utf-8"))
        self.counties[county_idx].insert(owner, gun)
    
    def delete(self, county_idx: int, owner: Owner, gun: Gun):
        self.scheme._Delete(self.edb, self.key, self.counters, gun.serial_number, bytes(str(county_idx), "utf-8"))
        self.counties[county_idx].delete(owner, gun)

if __name__ == "__main__":
    county_num = int(input("Enter the number of counties: "))
    state = State(county_num)
    
    query = 'a'
    
    print("""Possible Queries:
          sg - Search Global
          sl - Search Local
          i - insert
          d - delete
          q - quit
          """)

    while True:
        query = input("Enter a query: ")
        if query[0] == 'q':
            break
        elif query == "sg":
            serial_number = input("Enter serial number: ")
            print(state.search(bytes(serial_number, "utf-8")))
        elif query == "sl":
            county_idx = int(input("Enter the county index you want to search: "))
            serial_number = input("Enter serial number: ")
            print(state.search_county(bytes(serial_number, "utf-8"), county_idx))
        elif query[0] == "i":
            county_idx = int(input("Enter the county index needed for insertion: "))
            
            first_name = input("Enter owner's first name: ")
            last_name = input("Enter owner's last name: ")
            reg_num = input("Enter owner's registry number: ")
            phone_num = input("Enter owner's phone number: ")
            new_owner = Owner(first_name, last_name, reg_num, phone_num)
            
            ser_num = input("Enter serialization number for the gun: ")
            model = input("Enter the model of the gun: ")
            new_gun = Gun(ser_num, model)
            
            state.insert(county_idx, new_owner, new_gun)
            print(f"{first_name} {last_name} succesfully added.")
        elif query[0] == "d":
            county_idx = int(input("Enter the county index needed for insertion: "))
            
            first_name = input("Enter owner's first name: ")
            last_name = input("Enter owner's last name: ")
            reg_num = input("Enter owner's registry number: ")
            phone_num = input("Enter owner's phone number: ")
            new_owner = Owner(first_name, last_name, reg_num, phone_num)
            
            ser_num = input("Enter serialization number for the gun: ")
            model = input("Enter the model of the gun: ")
            new_gun = Gun(ser_num, model)
            
            state.delete(county_idx, new_owner, new_gun)
            print(f"{first_name} {last_name} succesfully removed.")
        else:
            print("Not a valid query.")
    
    