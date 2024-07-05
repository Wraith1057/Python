"""Description : Write a Python program to show difference between 'w' mode and 'a' mode of file.
"""
#difference between 'w' and 'a'
""" 'w' mode is used to write in the file
by overwriting existing content"""

a=open("trial.txt","w")
a.write("itv \n")
a.write("itv2 \n")

a=open("trial.txt","r")
print(a.read())

""" 'a' mode is used to write in the file
by adding content at the end without overwriting"""

a=open("trial.txt","a")
a.write("itv3 \n")

a=open("trial.txt","r")
print(a.read())