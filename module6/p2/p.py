#4. Read a file name “List.txt” from the user and a word and count occurrences of
#that word in the file.

f=open("list.txt","r")
b=f.read()
s=b.split()
j=0
for i in s :
	l=open(i,"r")
	g=l.read()
	k=g.count("is")
	j=j+k
	
print"the no.of 'is' ::: ", j
f.close()

