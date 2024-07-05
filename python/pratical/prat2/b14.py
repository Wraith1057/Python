"""Description : Write a Python program
to print lines with '*'.
"""
with open("abc.txt","r") as g:
    s=1
    c=g.read(s)
    while len(c)>0:
        print(c,end="*")
        c=g.read(s)