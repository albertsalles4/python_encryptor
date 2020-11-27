# -*- coding: utf-8 -*-
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


"""
This is a simple python file Encryptor which uses the cryptography library
"""
class Encryptor():
    
    def __init__(self, key=None):
        self.key = key
        self.salt = None
    
    def create_key(self):
        self.key = Fernet.generate_key()
        return self.key
    
    def write_key(self, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(self.key)
    
    def import_key(self, key_name):
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
                        
    def generate_random_salt(self):
        self.salt = os.urandom(16)
        return self.salt
        
    def write_salt(self, salt_name):
        with open(salt_name, 'wb') as mysalt:
            mysalt.write(self.salt)
    
    def import_salt(self, salt_name):
        with open(salt_name, 'wb') as mysalt:
            self.salt = mysalt.read()
    
    def load_salt(self, key):
        self.key = key
        
    def generate_key_with_password_and_salt(self, password, salt=None):
        if salt == None:
            if self.salt == None:
                self.generate_random_salt()
            
            salt = self.salt
        
        # We need a bytes-type password, not a string
        password = bytes(password, 'utf-8') 
            
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(password))
        