# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


# The random and string libraries are used to generate a random string with flexible criteria
import string
import random


# Random Key Generator
key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 1024))


print(key)

print ("\n" + "Key length = " + str(len(key)))

message = 'ipconfig'

print("Msg: " + message + '\n')




# here i defined a dedicated function called str_xor, we will pass two values to this fucntion, the first value is the message(s1) that we want to encrypt or decrypt, and the second paramter is the xor key(s2). We were able to bind the encryption and the decryption phases in one function because the xor operation is exactly the same when we encrypt or decrpyt, the only difference is that when we encrypt we pass the message in clear text and when we want to decrypt we pass the encrypted message


def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1,s2)])


# first we split the message and the xor key to a list of character pair in tuples format >>  for (c1,c2) in zip(s1,s2)

# next we will go through each tuple, and converting them to integer using (ord) function, once they converted into integers we can now perform exclusive OR on them  >>  ord(c1) ^ ord(c2)

# then convert the result back to ASCII using (chr) function  >>  chr(ord(c1) ^ ord(c2))
# last step we will merge the resulting array of characters as a sequqnece string using >>>  "".join function 








enc = str_xor(message, key)

print("Encrypted message is " + "\n" + enc + "\n")

dec = str_xor(enc, key)
print("Decrypted message is " + "\n" + dec + "\n")
