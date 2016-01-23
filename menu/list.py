# creat a program of multiput file user of choice 
print "MENU::\n 1:count the number of words\n 2:reading multiple files from untitled folder single text file\n 3:startswith function\n 4:endswith function \n 5:unigram count \n 5:bigram count\n 6:trigram count \n 7: for exit"
t=input("Type other than 8 to start") # taken some choices of input
while(t!=8):				# while loop
	choice=input("Enter your choice>>>::")# input asking to user 
	if (choice==1):				# if statment chaking
		f=open("list.txt","r")		# opening the file
		j=f.read()			# read the file
		k=j.split()			# split the words
		count=0				# taking the varable
		for i in k:			# for loop 
			a=open(i,"r")		# multi files opening 
			b=a.read()		# read the wordes
			c=b.split()		# split the wordes
			count=count+len(c)	# increment the varable
		print count			# printing statmen
	elif (choice==2):			
		f=open("list.txt","r")		# opening the file
		j=f.read()			# read the words 
		k=j.split()			#split the words
		count=0			
		for i in k:			# for loop
			a=open(i,"r")		# opening the multifile 
			b=a.read()		# read the words
			c=b.split(".")		# slit words
			count=count+len(c)	# increment the varable
		print count			# printing statmen
	elif (choice==3):
		f=open("list.txt")		# opening the file
		j=f.read()			# read the words
		k=j.split()			# split the words
		count=0			
		ch=raw_input("Enter character>>>::")# input asking to user 
		for i in k:			# for loop
			a=open(i,"r")
			b=a.read()
			c=b.split()
			for h in c:
				if (h[0]==ch):
					count=count+1	# increment the varable
		print count		# printing statmen
	elif (choice==4):
		f=open("list.txt")
		j=f.read()
		k=j.split()
		count=0
		ch=raw_input("Enter character>>>::")
		for i in k:
			a=open(i,"r")
			b=a.read()
			c=b.split()
			for h in c:
				if (h[-1]==ch):
					count=count+1# increment the varable
		print count # printing statmen
	elif (choice==5):
		f=open("list.txt","r")
		j=f.read()
		k=j.split()
		ch=raw_input("Enter your words of unigram>>>::")
		s_ch=ch.split()
		count=0
		for i in range(len(k)):
			a=open(k[i],"r")
			b=a.read()
			c=b.split()
			length=len(c)
			for i in range(length-1):
				if (c[i]==s_ch[0]):
					count=count+1 	# increment the varable
				else:
					continue
		if (count==0):
			print "The given unigram in Not Found" # printing statment
		else:
			print "yes The given unigram is Found",count,"times" # printing statmen
	elif (choice==6):
		f=open("list.txt","r")
		j=f.read()
		k=j.split()
		ch=raw_input("Enter your words of bigram>>>::") # asking to user input
		s_ch=ch.split()
		count=0
		for i in range(len(k)):
			a=open(k[i],"r")
			b=a.read()
			c=b.split()
			length=len(c)
			for i in range(length-1):
				if (c[i]==s_ch[0] and c[i+1]==s_ch[1]):
					count=count+1	# increment the varable
				else:
					continue
		if (count==0):
			print "The given bigram is Not Found"# printing statment
		else:
			print "yes, The given bigram is Found ",count,"times"
	elif (choice==7):
		f=open("list.txt","r")
		j=f.read()
		k=j.split()
		ch=raw_input("Enter your words of trigram>>>::")	# asking to user input
		s_ch=ch.split()
		count=0
		for i in range(len(k)):
			a=open(k[i],"r")
			b=a.read()
			c=b.split()
			length=len(c)
			for i in range(length-2):
				if (c[i]==s_ch[0] and c[i+1]==s_ch[1] and c[i+2]==s_ch[2]):
					count=count+1  # increment the varable
				else:
					continue
		if (count==0):
			print "The given trigram is Not Found" # printing statment
		else:
			print "yes, The given trigram is  Found",count,"times"
	else:
		t=8
		a.close()
	fil.close()
