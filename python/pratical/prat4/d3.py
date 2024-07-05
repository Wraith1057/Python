#Description : Program to show use of findall()

import re
var="The bat and a fat rat sat on a cat"
res=re.findall("[bfrsa]at",var)
print(res)