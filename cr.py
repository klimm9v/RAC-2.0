from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


salt = b'\x9e1\xc0\xc1\xe0\x163Fm\xec\xb6K\xc1L\x89:Z\x93\xec\xd7\x06*\xa7\x1d\xe9i$\x8e\x11\x0e}@'
password = 'mypassword'

key = PBKDF2(password, salt, dkLen=32)

message = b'\xfe\x10\x88\x14p\xc1D\xc4\x13\xd3\xbf\xb0\xd0z(\xcd\xd7\xd1(\xee.\\j}\x10\xf5Lw\xb8Y\x99\xbe'

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

