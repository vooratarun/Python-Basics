#1). Print the middle character for given odd length string?

a=raw_input("Enter string\n")   # taking  odd string
b=a.split()
c=len(a)/2    # half theentered string 
print "the middle  character in entered string is\n"
for i in b:
	print i[c]   # print middle char
