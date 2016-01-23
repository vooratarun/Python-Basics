f=open("trigram.txt","r")
a=f.read()
b=a.split()
print b
r=raw_input("Enter a tigram::\n")
s=r.split()
print s
c=0
for i in range(len(b)-2):
	if b[i]==s[0] and b[i+1]==s[1] and b[i+2]==s[2] :
		c=c+1
print "c:;",c
if c>0 :
	print "the given tigram is",c,"times in the file"
else :
	print "the trigram is not present in file"
f.close()
