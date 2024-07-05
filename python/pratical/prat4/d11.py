#8.use of sub
import re
phone='2004-959-559'

#delete python style comments
num=re.sub(r'-'," @ ",phone)
print("phone num",(num))

#remove anything other than digits
num=re.sub(r'\D'," ",phone)
print("phone num",(num))