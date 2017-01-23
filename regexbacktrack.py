# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = raw_input()
i = 0
while i<n :
    card_no = raw_input()
    xcard_no = re.sub(r'-', '', card_no)
    if re.search(r'([0-9])\1{3}' , xcard_no , re.I|re.M):
        print ("Invalid")
    elif len(xcard_no) > 16:
        print ("Invalid")
    elif re.match(r'[456][0-9]{15}', card_no , re.I| re.M):
        print ("Valid")
    elif re.match(r'[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}' , card_no , re.I|re.M):
        print ("Valid")
    else:
        print ("Invalid")
    i+=1