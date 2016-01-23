#Create a file with some text and save it as “bigram.txt”. Write a program
#to check the bigram(Take a trigram from the user) is in the file “bigram.txt”
#or not

f=open("t.txt","r")   #open a file
a=f.read()
b=a.split()
s=raw_input("Enter a bigram\n")  #taking input
k=s.split()   #splitting
c=0
for i in range(len(b)-1):
	if b[i]==k[0] and b[i+1]==k[1] :   # testing bigram
		c=c+1
	
print " ENtered string is ",c,"two times in file" 
if c>1 :
	print "bigram preset"  # print present or absent
else:
	print "bigram absent"
f.close()
