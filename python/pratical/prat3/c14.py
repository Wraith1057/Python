def fnc(level):
    if level<1:
        raise("Invalid level!",level)
try:
    print("business logic here")
except "Invalid level!":
    print("exception handling here")
else:
    print("rest of the code here")