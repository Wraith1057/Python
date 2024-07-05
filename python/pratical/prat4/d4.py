#Description : Program to show use of split()

import re
value="hey visitors, this is a program for split function"
#split() without parameters
res=value.split()
print ( res)
#split() with sep parameter
res=value.split(',')
print ( res)
#split() with sep parameter
res=value.split(' ',1) #space given as separator & 1 indicates maximum 1 split will be made
print ( res)