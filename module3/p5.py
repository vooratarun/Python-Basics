f=open("1.txt","r")
b=f.read()
d=b.split(" ")
c=0
for i in range(len(d)):
	k=d[i]
	for j in range(len(k)):
		if k[j].startswith("t") :
			c=c+1
print c
