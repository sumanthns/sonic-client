from Crypto.Cipher import AES
import base64
from config import CONF

def _cipher():
    secret_key = CONF.salt
    cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
    return cipher

def encrypt(msg_text):
    encoded = base64.b64encode(_cipher().encrypt(msg_text))
    return encoded

def decrypt(encoded):
    decoded = _cipher().decrypt(base64.b64decode(encoded))
    return decoded
