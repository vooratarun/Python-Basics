# finding frequency of unigrams in multiple files
f=open("list.txt","r")         # read a file containing multiple files
a=f.read() 
b=a.split() 
d={}
for j in b:                        
	g=open(j,"r")            # read each file in multiple files
	a=g.read()
	b=a.split()             # splitting the file
	for i in b :
		if i not in d :           # dictionary testing
			d[i]=1
		else :
			d[i]=d[i]+1

print d                        # printing all the files frequency
f.close()
