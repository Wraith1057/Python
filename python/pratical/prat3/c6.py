"""Description : Program to show try...except...else...finally
"""
try:
    val=int(input("enter a number"))
    x=100/val
except (ValueError):
    """ValueError exception is raised when any other value apart from integer datatype is passed"""
    print("I am 1st except clause")
    print("integer value expected")
except(ZeroDivisionError):
    """ZeroDivisionError exception is raised when we try to divide any number by 0"""
    print("I am 2nd except clause")
    print("non zero value expected")
else:
    print("I am else block and i will be executed if no exception is raised")
    print("result is  :",x )
finally:
    print("I am finally block and i will be executed even if exception is raised or not")