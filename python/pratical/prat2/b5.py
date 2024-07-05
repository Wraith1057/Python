#create file object and show the use tell()
object=open("itvoyagers.txt",'w')
object.write("first statement n")
object.write("second statement n")
object=open("itvoyagers.txt",'r')
s=11
c=object.read(s)
print(object.tell()) #tells the position based on parameter passed in read operation
g=object.read()
print(object.tell()) #tells position after performing read() on entire file