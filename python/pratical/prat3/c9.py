#Description : Program to check the age entered is in valid range

age=int(input("enter a your age"))
try:
    if age<0 or age>100:
        raise Exception(age) #here parameter is passed
    print("valid age ",age)
except Exception as e:
    print("age out of range ",e) 
#value for e is given out as parameter is passed in raise statement