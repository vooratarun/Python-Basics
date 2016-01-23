#1) Read a file name “list.txt” which has several file names. Count number of words in each file.

f=open("list.txt","r")  # opening list  containing several files
b=f.read()
s=b.split()   # splitting the file
l=0
for i in s :
	g=open(i,"r");  # open each file
	b=g.read()
	s=b.split(); 
	print "the no. of words in <<",i,">> file is   ",len(s)    # no.of words in each file
f.close()

