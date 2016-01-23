#2) Print all the last characters in the given file?

f=open("t.txt","r")   # open file
b=f.read()
c=b.split()   # splitting to words
print c
for i in c :
	print i[-1]    # print last chars
f.close()
