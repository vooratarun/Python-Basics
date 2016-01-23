f=open("t.txt","r")
b=f.read()
a=raw_input("Enter a string")
c=b.split()
print c
k=0
for i in c :
	if i==a :
		k=k+1
print "count is ",k
