try:
    f=open("abc.txt","w")
    f.write("test file for exception handling")
except IOError:
    print("Error:cannot find file")
else:
    print("contents are written succesfully in file")
    f.close()