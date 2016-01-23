a=raw_input("Enter a string::\n")
b=a.split()
x=raw_input("Enter character\n")
c=0
for i in range(len(b)):
	if b[i].startswith(x) :
		c=c+1
print c
	
