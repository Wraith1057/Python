"""Description : Program to use of seek()"""

#create file object and show the use seek()
with open("itvoyagers.txt","r") as f:
    s=10
    c=f.read(s) #reads till 10 char
    print(c,end=' ') #adds space after first read()
    f.seek(0,0) #goes to start position in file
    c=f.read(s)
    print(c)
    f.seek(0,1) #goes to current position in file
    c=f.read(s)
    print(c)
    f.seek(0,2) #goes to end position in file
    c=f.read(s)
    print(c)