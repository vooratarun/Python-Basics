# Read a file name “family.txt” which has several family member’s file names.
#Count the number of word “is” in each file, as well as the total number of times
#occurs in all the files

f=open("t.txt","r")
b=f.read()
a="is"
c=b.split()
print c
k=0
for i in c :
	if i==a :
		k=k+1
print "count is ",k
