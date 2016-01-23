#1) Print the true if the string has same first and last character?

a=raw_input("Enter a string")   #taking a string
print a[-1]  #last char
print a[0]  #firsr char
if a[-1]==a[0]:   # testing
	print "true"
