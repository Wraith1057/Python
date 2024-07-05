#user defined exception
class NotEquaLError(Exception):
    pass

n1=10
n2=9
try:
    if n1!=n2:
        raise NotEquaLError
    else:
        print("nos are equal")
except NotEquaLError:
    print("nums are not equal")