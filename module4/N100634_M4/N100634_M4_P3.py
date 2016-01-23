#3). Write a program to print the even characters in the given string”
#Country”?
a="country"   #string
b=a.split()		# splitting string
print "the letters in even places are \n"   
for i in range(len(a)) :
	if(i%2==1):         # checking even places
		for j in b :
			print j[i]
