f=open("abhi.txt",mode="w",encoding="utf-8")
print("file name is:",f.name)
print("Endoding is:",f.encoding)
print("Mode is:",f.mode)
print("is file closed?:",f.closed)
f.close()
print("is file closed?:",f.closed)