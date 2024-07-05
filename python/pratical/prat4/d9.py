#in given string search the full string,first string
import re
line="humans are intelligent than animals"
so=re.search(r'(.*) are (.*).*',line,re.M|re.I)
if so:
    print("so.group():",so.group())
    print("so.group(1):",so.group(1))
    print("so.group(2):",so.group(2))
else:
    print("no match found")