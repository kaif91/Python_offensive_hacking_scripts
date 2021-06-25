import ctypes

if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    print('[-] We are not admin')

else:
    print('[+] We are admin')