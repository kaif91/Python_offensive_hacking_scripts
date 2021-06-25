from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def encrypt(message):
    publickey = open("public.pem", "rb")
    public_key = RSA.importKey(publickey.read())
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted_data = encryptor.encrypt(message)
    print(encrypted_data)
    return encrypted_data

message = 'H'*470
encrypted_data = encrypt(message.encode())


def decrypt(cipher):
    privatekey = open("private.pem", "rb")
    private_key = RSA.importKey(privatekey.read())
    decryptor = PKCS1_OAEP.new(private_key)
    print (decryptor.decrypt(cipher).decode())

decrypt(encrypted_data)
