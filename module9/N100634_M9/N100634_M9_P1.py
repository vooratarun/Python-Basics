# total no. of occurances  of vowels in the given sentence

a=raw_input("enter a sentence")  # input a sentence 
v=[0,0]   # list declaration
for i in a:
	if i=='a' or i=='i' or i=='u'or i=='e' or i=='o':    # tesitng the vowels
		v[0]=v[0]+1
	elif i=='A' or i=='E' or i=='I'or i=='O' or i=='U':
		v[1]=v[1]+1
print "The small letter vowels in the program is",v[0]
print "The capital letter vowels in the program is",v[1]   # printing
