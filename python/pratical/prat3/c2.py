#Description : Program to show use of try...except...else block
try:
    val=int(input("enter a number"))
except ValueError:
    print("integer num expected")
else:
    print("number accepted")