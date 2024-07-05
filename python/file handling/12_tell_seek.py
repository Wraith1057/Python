#tell() method
f=open("abhi.txt",mode="r")
print(f.tell())             #shows the position of the cursor
f.read(3)                   #move the cursor to forward 3 space
print(f.tell())
f.read()                    #print the current position of the cursor
print(f.tell())
f.close()                   #close the file

#seek() method
f=open("abhi.txt",mode='r')
print(f.tell())             #pos 0
print(f.read(3))            #pos +3
f.seek(0)                   #pos back to 0
print(f.read())             
f.close()                   #close the file
