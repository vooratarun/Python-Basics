#Exercise problems:
#1. Create a file with some text and save it as “trigram.txt”. Write a program
#to check the trigram(Take a trigram from the user) is in the file “trigram.txt”
#or not.


f=open("trigram.txt","r") #open file
a=f.read()
b=a.split() #split by space
print b
r=raw_input("Enter a tigram::\n")  #input
s=r.split()
print s
c=0
for i in range(len(b)-2):
	if b[i]==s[0] and b[i+1]==s[1] and b[i+2]==s[2] :   #testing trigram
		c=c+1
print "c:;",c  #print count
if c>0 :
	print "the given tigram is",c,"times in the file"
else :
	print "the trigram is not present in file"
f.close()
