#prog to find length of each line of a file
f=open("abc.txt","r")
text=f.readlines()
print(text)
for line in text:
    print(len(line))