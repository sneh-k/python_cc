import email.utils
import re

n = raw_input()
i = 0
while i<n:
    email2 = raw_input()
    email1 = email.utils.parseaddr(email2)
    email1 = str(email1[1])
    #if re.match(r'[a-zA-Z]\w+@[a-zA-Z]*\.[a-zA-Z]{1,3}' , email1 , re.I | re.M):
        #print (email2)
    obj = re.split(r'([a-zA-Z][\w\.\-_]*@[a-zA-Z]+\.[a-zA-Z]{1,3})' , email1 , re.I | re.M)
    #print (obj)
    if len(obj) > 1 and obj[0] == '' and obj[2] == '':
        print (email2)