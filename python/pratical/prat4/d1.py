#Description : Program to show use of match()
import re
res= re.match(r'i','i am itvoyagers page')
res2=re.match(r'itvoyagers','i am itvoyagers page')
if res:
    print("match found",res.group())
else:
    print("match not found")
if res2:
    print("match found",res2.group())
else:
    print("match not found")