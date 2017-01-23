# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = raw_input()
i = 0
flag = 0
while i<n :
    flag = 0
    card_no = raw_input()
    xcard_no = re.sub(r'-', '', card_no)
    obj = re.split(r'([0-9])\1{3}', xcard_no, re.I | re.M)
    if len(obj) > 1:
        print ("Invalid")
        flag = 1
    elif len(xcard_no) > 16:
        print ("Invalid")
        flag = 1
    elif re.match(r'[456][0-9]{15}', card_no , re.I| re.M) and flag == 0:
        print ("Valid")
    elif re.match(r'[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}' , card_no , re.I|re.M) and flag == 0:
        print ("Valid")
    elif flag == 0:
        print ("Invalid")
    i+=1