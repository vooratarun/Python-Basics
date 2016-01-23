a="ram ram tarun tarun python python python"
d={}
b=a.split()
for i in  b :
	if i not in d :
		j=i
		d[j]=1
	else :
		j=i
		d[j]=d[j]+1
print "The DICTIONARY IS \t",d
print"--------------------------------------"
print d.items()
print "The keys are",d.keys()
print "The values are",d.values()
print "------------------------------------"
for k,v in d.iteritems():
	print k,v
print "--------------------------"
for i,v in enumerate(d.keys()):
	print i,v
print "-------------------------------------"
print d.has_key("ram")
print "get function",d.get("ram")
print d.clear()

