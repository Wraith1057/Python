#search 
import re
print('\n find the digits')
print(re.findall(r'\d','meera 123456 road'))
print('\n find the non digits')
print(re.findall(r'\D','meera 123456 road'))
print('\n find the non spaces')
print(re.findall(r'\S','meera 123456 road'))