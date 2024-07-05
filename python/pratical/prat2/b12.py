"""Description : Write a Python program to read
lines by applying loop on file object
"""
f=open("abc.txt","r")
for line in f:
    print(line ,end=" ")