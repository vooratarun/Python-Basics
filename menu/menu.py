def tarun():
	print "|_______________________________________________________________________________|"
	print "|...................MENU.......................................	................|"
	print "|	1.search a word in the  file     					|"
	print "|	2.enter a char to find the words starts with that word			|"
	print "|	3.enter a char to find the words ends with that word			|"
	print "|	4.for unigram								|"
	print "|	5.bigram								|"
	print "|	6.tigram								|"
	print "|	7.For no. of words in each file						|"
	print "|	8.click for exit							|"
	print "|...............................................................................|"
	print "|_______________________________________________________________________________|"
tarun()
a=0
while(a!=8):
	a=input("Enter the choice\n")
	if a==1 :
		f=open("list.txt","r")
		a=f.read()
		b=a.split()
		j=0
		z=raw_input("Enter a word")
		for i in b :
			l=open(i,"r")
			g=l.read()
			k=g.count(z)
			j=j+k
		if j>0 :
			print "Entered string is present in file"
		else :
			print "Entered string is absent in file"
		f.close()
		print tarun()
	elif a==2 :
		f=open("list.txt","r")
		a=f.read()
		b=a.split()
		x=0
		z=raw_input("Enter a character")
		for i in b :
			l=open(i,"r")
			g=l.read()
			h=g.split(" ")
			c=0
			for j in range(len(h)):
				k=h[j]
				for j in range(len(k)):
					if k[j].startswith(z) :
						c=c+1
				x=x+c
		print "total words ::",x

		f.close()
		print tarun()
	elif a==3 :
		f=open("list.txt","r")
		a=f.read()
		b=a.split()
		x=0
		z=raw_input("Enter a character")
		for i in b :
			l=open(i,"r")
			g=l.read()
			h=g.split(" ")
			c=0
			for j in range(len(h)):
				k=h[j]
				for j in range(len(k)):
					if k[j].endswith(z) :
						c=c+1
			x=x+c
		print "total words ::",x	
		f.close()
		print tarun()	

	elif a==4 :
		f=open("list.txt","r")
		a=f.read()
		b=a.split()
		j=0
		z=raw_input("Enter a word")
		for i in b :
			l=open(i,"r")
			g=l.read()
			k=g.count(z)
			j=j+k
		print"the given unigram ",j,"times in file"
		f.close()
		print tarun()
	elif a==5 :
		f=open("list.txt","r")
		a=f.read()
		b=a.split()
		k=raw_input("etner  a trigram\n");
		l=k.split()
		print l[0]
		z=0
		for i in b :
			g=open(i,"r")
			print "\t i ::",i
			h=g.read()
			s=h.split()
			c=0
			for i in range(len(s)-1):
				if s[i]==l[0] and s[i+1]==l[1] :
					c=c+1
					print "c::",c
			z=z+c			
		print "The entered bigram is ",z,"times in book"
		f.close()
		print tarun()
	elif a==6 :
		f=open("list.txt","r")
		a=f.read()
		b=a.split()
		k=raw_input("etner  a trigram\n");
		l=k.split()
		print l[0]
		z=0
		for i in b :
			g=open(i,"r")
			print "\t i ::",i
			h=g.read()
			s=h.split()
			c=0
			for i in range(len(s)-2):
				if s[i]==l[0] and s[i+1]==l[1] and s[i+2]==l[2] :
					c=c+1
					print "c::",c
			z=z+c			
		print "The entered trigram is ",z,"times in book"
		f.close()
		print tarun()
	elif a==7 :
		f=open("list.txt","r")
		b=f.read()
		s=b.split()
		l=0
		for i in s :
			g=open(i,"r");
			b=g.read()
			s=b.split();
			print "the no. of words in <<",i,">> file is   ",len(s)
			l=l+len(s)
		print "total  words in the book is",l

		f.close()
		print tarun()
	elif a==8 :
		a==8


