# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = raw_input()
i = 0
while i < n:
    colorcode = raw_input()
    if re.search(r'{',colorcode):
        colorcode = raw_input()
        i += 1
        while colorcode != '}':
            obj = re.findall(r'#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3}', colorcode, re.I | re.M)
            for s in obj:
                print s
            colorcode = raw_input()
            i += 1

