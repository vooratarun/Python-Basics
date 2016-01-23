f=open("t.txt","r")
b=f.read()
d=b.split(" ")
print d
c=0
for i in range(len(d)):
	k=d[i]
	for j in range(len(k)):
		if k[j].startswith("s") :
			c=c+1
print c-1
