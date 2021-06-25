from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def decrypt(cipher):
    privatekey = open("private.pem", "rb")
    private_key = RSA.importKey(privatekey.read())
    decryptor = PKCS1_OAEP.new(private_key)
    print (decryptor.decrypt(cipher).decode())


def encrypt(message):
    publickey = open("public.pem", "rb")
    public_key = RSA.importKey(publickey.read())
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted_data = encryptor.encrypt(message)
    print(encrypted_data)
    decrypt(encrypted_data)

message = 'H'*500

if len(message) > 470:
    for i in range(0, len(message), 470):
        chunk = message[0+i:470+i]
        encrypt(chunk.encode())
else:
    encrypt(message.encode())
