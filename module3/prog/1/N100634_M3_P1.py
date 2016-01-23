f=open("list.txt","r")
b=f.read()
s=b.split()
l=0
for i in s :
	g=open(i,"r");
	b=g.read()
	s=b.split();
	print "the no. of words in <<",i,">> file is   ",len(s)
	l=l+len(s)
print "total  words in the book is",l

f.close()

