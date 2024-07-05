#Description : Program to show try...except...else...finally

try:
    val=int(input("enter a number"))
    x=100/val
except (ValueError):
    print("I am 1st except clause")
    print("integer value expected")
else:
    print("I am else block and i will be executed if no exception is raised")
    print("result is  :",x )
finally:
    print("I am finally block and i will be executed even if exception is raised or not")