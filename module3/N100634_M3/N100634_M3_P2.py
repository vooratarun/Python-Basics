#2) Read a file name 'list.txt' which has several file names. Each file is a chapter in a Telugu text
#book. Count the number of words in each file, as well as the total number of words in all the files.

f=open("list.txt","r")   # open  list file
b=f.read()
s=b.split()
l=0
for i in s :
	g=open(i,"r");   # oepn each file
	b=g.read()
	s=b.split();
	print "the no. of words in <<",i,">> file is   ",len(s)  # words in each file
	l=l+len(s)                            # summing up all the file's words
print "total  words in the book is",l   # printing the words in  book

f.close()

