# finding frequency of the unigram in one file
f=open("1.txt","r")        # opening file
a=f.read()           # read
b=a.split()        #split
d={}
for i in b :                # testing if the word is present in dictionary or not
	if i not in d :
		d[i]=1
	else :
		d[i]=d[i]+1

print d                    # printing dictionary
f.close()
