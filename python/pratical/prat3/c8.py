# Program to check the age entered is in valid range using 
age=int(input("enter a your age"))
try:
    if age<0 or age>100:
        raise Exception() #here no parameter is passed
    print("valid age ",age)
except Exception as e:
    print("age out of range ",e) 
#no value for e is given out as no parameter is passed in raise statement