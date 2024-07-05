#programme to calculate words, characters and lines
f=open("abhi.txt",mode='r')
num_of_words=0
num_of_char=0
num_of_lines=0
for line in f:
    num_of_lines+=1
    line=line.strip("\n")
    num_of_char+=len(line)
    list1=line.split()
    num_of_words+=len(list1)
f.close()
print("Number of lines:",num_of_lines)
print("Number of character:",num_of_char)
print("Number of words:",num_of_words)