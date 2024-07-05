"""Description :  Write a Python program to read an entire text file."""
def file_read(filename):
        #open() is used to open a file and to create a file object
        #txt is file object
        txt = open(filename)  
        print(txt.read()) #read() is used to read entire data in file 
file_read('itvoyagers.txt') #text file must be created priorly