def tarun(File,k) :
	f=open(File,"r")
	a=f.read()
	b=a.split()
	c=0
	for some in b :
		if some==k :
			c=c+1
	print File,"contains",c,"times entered strings"
	
f=open("list.txt","r")
a=f.read()
b=a.split()
k=raw_input("Enter a string")
for i in b:
	 tarun(i,k)


