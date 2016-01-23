f=open("2.txt","r")
a=f.read()
t=0
c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
g=0
b=[]
print "\tSMALL  LETTERS IN THE FILE"
for  i in c :
	g=i
	c=0
	for j in a:
		if g==j:
			c=c+1
			b.append(c)
print "The list is",b
print "\tCAPITAL LETTERS IN THE FILE "
for  i in d :
	g=i
	b=[0]
	for j in a:
		if g==j:
			b[0]=b[0]+1
	if b[0]>0 :
		t=t+b[0]
		print "\t",g,"\t::",b[0]
print "THE TOTAL NO. OF ALL CAPITAL AND SMALL CHARACTORS ARE ",t
f.close()
