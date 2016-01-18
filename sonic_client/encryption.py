from Crypto.Cipher import AES
import base64
from sonic_client.config import CONF

secret_key = CONF.get("client", "salt") # create new & store somewhere safe

cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously

def encrypt(msg_text):
    encoded = base64.b64encode(cipher.encrypt(msg_text))
    return encoded

def decrypt(encoded):
    decoded = cipher.decrypt(base64.b64decode(encoded))
    return decoded
