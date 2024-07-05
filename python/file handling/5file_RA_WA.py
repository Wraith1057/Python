#for read operation
f=open("abhi.txt",mode="r")
print(f.readable())
print(f.writable())
f.close()

#for write operation
f=open("abhi.txt",mode="w")
print(f.readable())
print(f.writable())
f.close()

#for read & write operation together with print statement
f=open("abhi.txt",mode='r')
# f=open("abhi.txt",mode='w')
if f.readable():
    print("file is readable")
f.close()