#Types of ways to close the file

#1st. Normal Form
f=open("abhi.txt",mode='r')
#operation like Read & Write
f.close()

#2nd. Using Exception Handling
try:
    f=open("abhi.txt",mode='r')
    #operation like Read & Write
finally:
    f.close()

#3rd. Using Statements
with open("abhi.txt",mode='r') as f:
    #operations

#with open("abhi.txt",mode='r') as f:
    data=f.read()
    print(data)
