from cryptography.fernet import Fernet
import re
import ctypes
import time
import os
import sys

class Credentials():
  
    def __init__(self, username, password, _username, expiry_time=-1):

        self.encrypt(username, password, _username)
        self.expiry_time = expiry_time
        self.f_key= 'pvt.key'
        self.f_cred = 'credentials.ini'
  
    def create_cred(self):
        with open(self.f_cred,'w') as file_in:
            file_in.write("#Credentials \nUsername={}\nPassword={}\n_Username={}\nExpiry={}\n"
            .format(self.username,self.password,self._username, self.expiry_time))
            file_in.write("++"*18)
  
        if(os.path.exists(self.f_key)):
            os.remove(self.f_key)
  
        try:
            with open(self.f_key,'w') as key_file:
                key_file.write(self.key.decode())
                ctypes.windll.kernel32.SetFileAttributesW(self.f_key, 2)
            print("cred file created successfully : {}".format(self.f_cred))
        except PermissionError:
            os.remove(self.f_cred)
            os.remove(self.f_key)
            print("permission denied : operation failed")
            sys.exit()

    @staticmethod
    def read_cred(f_cred, f_key):

        with open(f_key,'r') as key_file:
            key = key_file.read().encode()
        os.remove(f_key)

        fernet = Fernet(key)

        with open(f_cred,'r') as cred_file:
            lines = cred_file.readlines()
            config = {}
            for line in lines:
                tuples = line.rstrip('\n').split('=',1)
                if tuples[0] in ('Username','Password', '_Username'):
                    config[tuples[0]] = tuples[1]
            username = fernet.decrypt(config['Username'].encode()).decode()
            password = fernet.decrypt(config['Password'].encode()).decode()
            _username = fernet.decrypt(config['_Username'].encode()).decode()
        return (username, password, _username)

    
    def encrypt(self, username, password, _username):
        self.key = Fernet.generate_key()
        self.username = Fernet(self.key).encrypt(username.encode()).decode()
        self.password = Fernet(self.key).encrypt(password.encode()).decode()
        self._username = Fernet(self.key).encrypt(_username.encode()).decode()


#uncomment and encryt credentials (.ini)
# EXPIRY_TIME = -1
# USERNAME = "email"
# PASSWORD = "password"
# _USERNAME = "email"
# creds = Credentials(username=USERNAME, password=PASSWORD, _username=_USERNAME)
# creds.create_cred() 