# compute unique words and their frequency in the sentence by using dictionary

a="ram ram tarun tarun python python python"                    # sentence
d={}										    # empty dictonary
b=a.split() # splitting the sentence
for i in  b :                   # taking a loop
	if i not in d :       # checking if a word present in the dictionary or not
		d[i]=1     
	else :
		d[i]=d[i]+1     # if present increment as one
print "The DICTIONARY IS \t",d,"\n"         # printing dictionary
print "\tkeys","\tvalues"
print "\t............."						
for i in d :
	print "\t",i,"\t",d[i]
