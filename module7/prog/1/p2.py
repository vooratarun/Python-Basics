f=open("list.txt","r")
a=f.read()
b=a.split()
k=raw_input("etner word\n");
l=k.split()
z=0
for i in b :
	g=open(i,"r")
	h=g.read()
	s=h.split()
	c=0
	for i in range(len(s)-1):
		if s[i]==l[0] and s[i+1]==l[1] :
			c=c+1
			
	z=z+c			
print "The entered bigram is ",z,"times in book"
f.close()
