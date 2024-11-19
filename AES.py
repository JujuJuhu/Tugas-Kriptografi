import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
 
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
key = "262731621gvhdwfd7237e623" #a constant key is maintain on both side encryption and decryption
 
 
def encrypt(raw, key):
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    raw = str.encode(pad(raw)) #convert str to byte 
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
 
 
def decrypt(enc, key):
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))
 
#----------------------------------
#.........Encryption...............
message = "This is a secret message"
encrypted = encrypt(message, key)
print(encrypted)
 
#----------------------------------
#.........Decryption...............
decrypted = decrypt(encrypted, key)
print(bytes.decode(decrypted))