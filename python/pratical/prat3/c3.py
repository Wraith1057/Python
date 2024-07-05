#Description : Program to show except clause with  multiple attributes
try:
    val=int(input("enter a number"))
    x=100/val
except (ValueError,ZeroDivisionError):
    print("non zero integer expected")
else:
    print("result is  :",x )