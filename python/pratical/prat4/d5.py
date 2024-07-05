#Description : Program to show use of sub()
import re
date="2019-01-30"
pat=re.sub('-',' ',date) #it will replace - with space
print(pat)
op=re.sub('-',' ',date,1) #it will replace - with space but only for 1 occurance
print(op)
non_dig=re.sub('-',': ',date)
print(non_dig)