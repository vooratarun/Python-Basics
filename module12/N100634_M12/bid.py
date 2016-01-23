f=open("1.txt","r")
a=f.read()
b=a.split()
d={}
for i in range(len(b)-1) :
	x=b[i]+ '  '+b[i+1]
	if x not in d :
		d[x]=1
	else :
		d[x]=d[x]+1

print d
f.close()
