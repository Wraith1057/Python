#1:Description : Program to check the number entered is integer using exeception handling
try:
    val=int(input("enter a number"))
    print("value accepted")
except ValueError:
    print("integer number expected")
