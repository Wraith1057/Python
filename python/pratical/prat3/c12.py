try:
    fh=open("itvoyagers","r+")
    try:
        fh.write("Exception handling")
    finally:
        print("going to close")
        fh.close()
except IOError:
    print("can't find file/read data")