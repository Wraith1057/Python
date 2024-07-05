import random
import string

print("welcome to password generator")

lower=string.ascii_lowercase  #a-z
upper=string.ascii_uppercase  #A_Z
digit=string.digits           #0-9
symbol=string.punctuation     #Symlols

all=lower+upper+digit+symbol
length=int(input("Enter the length of password:"))
password=random.sample(all,length)
password="".join(password)

print("password is:",password)
