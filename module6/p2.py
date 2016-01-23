a="i am tarun. i am in iiit"
b=a.split()
print b
c=0
for i in range(len(b)) :     			## or we write for i in b, then we write  if i=="am" then c=c+1
	if (b[i]=="am") :
		c=c+1
print "the count is",c
