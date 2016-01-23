f=open("list.txt","r")
a=f.read()
b=a.split()
s=0
for i in b:
	g=open(i,"r")
	print"\n\t",i
	a=g.read()
	v=[0,0,0,0,0]
	for i in a:
		if i=='a' :
			v[0]=v[0]+1
		elif i=='e' :
			v[1]=v[1]+1
		elif i=='i' :
			v[2]=v[2]+1
		elif i=='o' :
			v[3]=v[3]+1
		elif i=='u' :
			v[4]=v[4]+1
	s=s+v[0]+v[1]+v[2]+v[3]+v[4]
	print " \t'a' ::",  v[0],"\n\t'e'::",  v[1],"\n\t'i' ::",  v[2],"\n\t'o'::",  v[3],"\n\t'u'::",  v[4],"\n\t"
print "Tworal no. of  vowels in the book is",s
f.close()
