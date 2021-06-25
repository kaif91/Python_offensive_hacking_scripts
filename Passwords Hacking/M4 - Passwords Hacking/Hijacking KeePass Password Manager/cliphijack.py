# Python For Offensive PenTest: A Complete Practical Course- All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


#pip install pyperclip

import pyperclip 
import time

list = [] # we create a list which will store the clipboard content

while True: # infifnite loop to continously check the  clipboard

    if pyperclip.paste() != 'None': # if the clipboard content is not empty ...
        value = pyperclip.paste() # then we will take its value and put it into variable called value

#now to make sure that we don't get replicated items in our list before appending the value varaible into our list, we gonna check if the value is stored eariler in the first place, if not then this menas this is a new item and we will append it to our list


        if value not in list:
            list.append(value)

        print(list)

        time.sleep(3)
