"""Description : Write a Python program to read last n lines of a file.
"""
f=open('itvoyagers.txt','r')
#readlines() is used to read entire file and returns list of lines
list_of_lines=f.readlines() 
n=int(input("enter number of of lines"))
print(list_of_lines[-n])
f.close() #close() performs clean up activities