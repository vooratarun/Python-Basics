#2. Take the file “list.txt”( which you have in the previous module with names
#of multiple files) and write a python program to print how many times given
#trigram(Take from the user) is found.

f=open("list.txt","r")   #open list 
a=f.read()
b=a.split()
k=raw_input("etner  a trigram\n");  #taking input
l=k.split()
print l[0]
z=0
for i in b :
	g=open(i,"r")  # open eachfile in the list file
	print "\t i ::",i
	h=g.read()
	s=h.split()
	c=0
	for i in range(len(s)-2):
		if s[i]==l[0] and s[i+1]==l[1] and s[i+2]==l[2] :  # count trigrams in each files
			c=c+1
			print "c::",c
	z=z+c			# sum of all trigrams in all files
print "The entered trigram is ",z,"times in book"  #printing
f.close()
