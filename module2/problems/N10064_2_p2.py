#Count the No of characters with space and without spaces separately in the given file name
f=open("tarun.txt","r")   #opening file
g=f.read()      #reading file
b=0
for i in g:
	b=b+1; 
	s=g.count(" ")   # countinng the spaces
l=b-1
print "THE NO. OF CHARACTERS IN A GIVEN FILE WITH SPACES  :",l  #printing no.of chars
print "THE NO. OF CHARACTERS IN A GIVEN FILE WITHOUT SPACES  :",l-s   
f.close()
