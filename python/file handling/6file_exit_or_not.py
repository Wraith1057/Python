import os
f = input ("Enter the file name:")
if os.path.isfile(f):
    f=open("abhi.txt")
    f.close()
    print("File exist")
else:
    print("File not exist") 