"""Description : Write a Python program to print
specified characters from a file.
"""
with open("abc.txt","r") as f:
    c=f.read(11)
    print(c)