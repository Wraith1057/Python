"""Description : Program to use of write() and writelines()"""

#create file object and open file in write mode
object=open("itvoyagers.txt",'w')
object.write("first statement \n")
object.write("second statement \n")
bulk=("This is Itvoyagers blog","\n this is python practical","\n this is to check use of writelines function")
object.writelines(bulk)
object=open("itvoyagers.txt",'r')
c=object.read()
print(c)