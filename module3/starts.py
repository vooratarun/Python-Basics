f=open("list.txt","r")
b=f.read()
s=b.split()
su=0
for i in s :
	g=open(i,"r");
	print i
	b=g.read()
	d=b.split(" ");
	c=0
	for j in range(len(d)):
		k=d[j]
		for l in range(len(k)):
			if k[l].startswith("g") :
				c=c+1
	su=su+c
				

print su
