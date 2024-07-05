#with space by \n
f=open("abhi.txt",mode="r")
data=f.readlines()
for line in data:
    print(line)
f.close()

#with no space by \n
f=open("abhi.txt",mode="r")
data=f.readlines()
for line in data:
    print(line,end="")
f.close()