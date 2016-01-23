f=open("list.txt","r")
a=f.read()
b=a.split()
k=raw_input("etner  a trigram\n");
l=k.split()
print l[0]
z=0
for i in b :
	g=open(i,"r")
	print "\t i ::",i
	h=g.read()
	s=h.split()
	c=0
	for i in range(len(s)-2):
		if s[i]==l[0] and s[i+1]==l[1] and s[i+2]==l[2] :
			c=c+1
			print "c::",c
	z=z+c			
print "The entered trigram is ",z,"times in book"
f.close()
