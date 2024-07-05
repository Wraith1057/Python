#Description : Program to show multiple except clause 
try:
    val=int(input("enter a number"))
    x=100/val
except (ValueError):
    print("integer value expected")
except(ZeroDivisionError):
    print("non zero value expected")
else:
    print("result is  :",x )