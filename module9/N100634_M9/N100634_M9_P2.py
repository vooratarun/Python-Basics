# find the vowels in the given file (case sensitive)
f=open("1.txt","r")  # open a fle
a=f.read() # read a file
v=[0,0,0,0,0]    # declaration of a list
s=0
for i in a:
	if i=='a' or i =='A' :      # checking the vowel
		v[0]=v[0]+1
	elif i=='e' or i=='E' :
		v[1]=v[1]+1
	elif i=='i' or i=='I':
		v[2]=v[2]+1
	elif i=='o' or i=='O':
		v[3]=v[3]+1
	elif i=='u' or i=='U' :
		v[4]=v[4]+1
s=s+v[0]+v[1]+v[2]+v[3]+v[4]              # summing up all the vowels 
print " \t'a,A' ::",  v[0],"\n\t'e,E'::",  v[1],"\n\t'i,I' ::",  v[2],"\n\t'o,O'::",  v[3],"\n\t'u,U'::",  v[4]               # printing the vowels characterwise
print "Tworal no. of  vowels in the book is",s
f.close()
