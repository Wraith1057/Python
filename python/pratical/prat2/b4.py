"""Description : Program to use of append mode and to
show difference in write and append modes
"""
#create file object and open file in append mode
object=open("itvoyagers.txt",'w') #creates file and with write mode and added strings
object.write("first statement \n")
object.write("second statement \n")
"""if we use same object to open another file or 
same file in different mode we do not need to use object.close()"""
object=open("itvoyagers.txt",'r')
c=object.read()
print("statements written using write mode \n",c)
object=open("itvoyagers.txt",'a') #added more strings without overwriting using append mode
object.write("third statement \n")
object=open("itvoyagers.txt",'r')
c=object.read()
print("statements written using append mode \n",c)
object=open("itvoyagers.txt",'w') #added strings by overwriting using write mode
object.write("fourth statement \n")
object=open("itvoyagers.txt",'r')
c=object.read()
print("statements written using write mode \n",c)