import base64

encoded = base64.b64encode(bytes('333222111','ascii'))

print(encoded)

decoded = base64.b64decode(encoded)
print(str(decoded)[2:-1])