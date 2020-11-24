# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet

"""
This is a simple python file Encryptor which uses the cryptography library
"""
class Encryptor():
    
    def __init__(self, key=None):
        self.key = key
    
    def create_key(self):
        self.key = Fernet.generate_key()
        return self.key
    
    def key_write(self, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(self.key)
    
    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            self.key = mykey.read()
        return self.key
    
    def is_key_loaded(self):
        return self.key != None
    
    def encrypt_file(self, original_file, encrypted_file=None):
        if encrypted_file is None:
            encrypted_file = original_file
        
        f = Fernet(self.key)
        
        
        with open(original_file, 'rb') as fi:
            original = fi.read()
            
        encrypted = f.encrypt(original)
        
        with open(encrypted_file, 'wb') as fi:
            fi.write(encrypted)
    
    def decrypt_file(self, encrypted_file, decrypted_file=None):
        if decrypted_file is None:
            decrypted_file = encrypted_file
        
        f = Fernet(self.key)
        
        with open(encrypted_file, 'rb') as fi:
            encrypted = fi.read()
        
        decrypted = f.decrypt(encrypted)
        
        with open(decrypted_file, 'wb') as fi:
            fi.write(decrypted)
                        
        
        