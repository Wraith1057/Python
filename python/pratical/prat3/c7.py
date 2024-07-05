#Example to show single exception as argument
try:
    val=int(input("enter a num"))
    result=100/val
except Exception as e:
    print("the argument is having value as", e)
    print("exception",type(e))
else:
    print("no exception so result is",result)