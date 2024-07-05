f1=open("abhi.txt", mode='r', encoding='utf-8')
f2=open("01.txt", mode='w', encoding='utf-8')
for line in f1:
    f2.write(line)
