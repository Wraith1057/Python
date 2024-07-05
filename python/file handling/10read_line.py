# #to read single line
f=open("abhi.txt",mode="r")
data=f.readline()
print(data)
f.close()

# #to read multiple line
f=open("abhi.txt",mode="r")
data1=f.readlines()
print(data1)
f.close()

#to read single and multiple lines at once
f=open("abhi.txt",mode="r")
data=f.readline()
data1=f.readlines()
print(data,end="")
print(data1,end="")
f.close()

