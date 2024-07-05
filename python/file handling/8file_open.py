#using read operation
f=open("abhi.txt",mode="r")
data=f.read()
print(data)
f.close()

#using read+binary operation
f=open("abhi.txt",mode="rb")
data=f.read()
print(data)
f.close()