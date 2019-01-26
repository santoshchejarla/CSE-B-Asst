import base64
import binascii
a='asd'.encode()
encoded = base64.b64encode(a)
print(encoded)
decoded = base64.b64decode(encoded)
print(decoded.decode())