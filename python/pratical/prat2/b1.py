#python program to show use of file attributes
#create file object and open file in any suitable mode like 'wb'
obj=open('itvoyagers.txt','wb')
print("name of a file",obj.name)
print("mode of a file",obj.mode)
print("file open or close",obj.closed)
print("softspace flag",obj.softspace)