import re

n = raw_input()
i = 0
while i<n:
    colorcode = raw_input()
    print (re.findall(r'#[A-F0-9]{3}',colorcode,re.I))
    #print (re.findall(r'#[A-F0-9]{6}|#[A-F0-9]{3}', colorcode , re.I | re.M))