#2. Take the file “list.txt”( which you have in the previous module
#with names of multiple files) and write a python program to print
#how many times given bigram(Take from the user) is found.


f=open("list.txt","r")     #open list file
a=f.read()
b=a.split()
k=raw_input("etner word\n");  #input taking
l=k.split()
z=0
for i in b : 
	g=open(i,"r")    # reading each file from list of files
	h=g.read()
	s=h.split()
	c=0
	for i in range(len(s)-1):
		if s[i]==l[0] and s[i+1]==l[1] :
			c=c+1    #countin bigrams from each file
			
	z=z+c			#summing up	all the file's	 bigrams
print "The entered bigram is ",z,"times in book"
f.close()
