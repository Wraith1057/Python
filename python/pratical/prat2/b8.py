"""
Description : Write a Python program to append text to a file and display the text.
"""
#'a' mode can create a file if it does not exist
f=open('abc.txt','a')
#write() is used to write text into file in both 'a' and 'w' modes
f.write("easy to learn \n")
f=open('abc.txt','r')
container=f.read()
print(container)
f.close()