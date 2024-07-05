#Description : Program to show use of search()
import re
res= re.search(r'i','i am itvoyagers page')
res2=re.search(r'itvoyagers','i am itvoyagers page')
if res:
    print("match found",res.group())
else:
    print("match not found")
if res2:
    print("match found",res2.group())
else:
    print("match not found")