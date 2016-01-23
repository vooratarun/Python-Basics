# finding frequency of the bigram in the given multiple files
f=open("list.txt","r")          # read the file containing multiple files
a=f.read() 
b=a.split()
d={}
for j in b:
	g=open(j,"r")           # read each file
	a=g.read()
	b=a.split()           # splitting the file 
	for i in range(len(b)-1) :       # take the words using length
		x=b[i]+' '+b[i+1]          # adding  first unigram and second unigram to complete our necessary bigram
		if x not in d :
			d[x]=1             # test with bigram
		else :
			d[x]=d[x]+1

print d                # printing dictionary 
f.close()
