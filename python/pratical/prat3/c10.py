#user defined exceptions
class MyErrorClass(Exception):
    pass
val=int(input("enter the number"))
try:
    if val!=100:
        raise MyErrorClass #user defined Exception classname
except MyErrorClass:
    print("Exception raised value no matched")
else:
    print("value matched")