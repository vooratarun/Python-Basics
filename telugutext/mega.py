def menu():									#menu function
	print "===================== MENU ==========================="
	print "|Press  1 \t for \t File names                 |"
	print "|       2 \t for \t Words count in files       |"
	print "|       3 \t for \t Unigram search             |"
	print "|       4 \t for \t Bigram search              |"
	print "|       5 \t for \t Trigram search             |"
	print "|       6 \t for \t Display content            |"
	print "|       7 \t for \t exit                       |"
	print "|       0 \t for \t MENU                       |"
	print "======================================================"
menu()
i=0
while(i!=7):
	choice=input("Enter ur choice  >>>  ")
	if(choice==0):
		menu()
	elif(choice==1):
		f=open("list.txt","r")
		a=f.read()
		print "Files in list.txt are >>>> \n",a
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. end of case1<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	elif(choice==2):
		f=open("list.txt","r")
		a=f.read()
		b=a.split()
		total=0
		print "        File name      \t\t      words"
		print"       ============     \t  ============="
		for i in b:
			fn=open(i,"r")
			c=fn.read()
			s=c.split()
			print i,"\t\t",len(s)
			total=total+len(s)
		print "\n================================================"
		print "total is  : ",total
		print "\n================================================"
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. end of case2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
	elif(choice==3):
		se=raw_input("Enter uigram for search >> ")
		f=open("list.txt","r")
		a=f.read()
		b=a.split()
		count=0
		for i in b:
			fn=open(i,"r")
			c=fn.read().count(se)
			count+=c
		print "(",se,")"," is found ",count," times"
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> end of case3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	
	elif(choice==4):
		f=open("list.txt","r")
		a=f.read()
		b=a.split()
		s=0
		search=raw_input("Enter a bigram for search in list.txt >>>  ")
		e=search.split()
		for i in b:
			fn=open(i,"r")
			c=fn.read()
			d=c.split()
			count=0
			for i in range(len(d)-1):
				if(d[i]==e[0] and d[i+1]==e[1]):
					count+=1
				else:
					continue
			s=s+count
		if(count==0):
			print "NOT FOUND"
		else:
			print search," Is  Found ",s,"times" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> end of case4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<			
	elif(choice==5):
		f=open("list.txt","r")
		a=f.read()
		b=a.split()
		s=0
		search=raw_input("Enter a trigram for search in list.txt >>>  ")
		e=search.split()
		for i in b:
			fn=open(i,"r")
			c=fn.read()
			d=c.split()
			count=0
			for i in range(len(d)-2):
				if(d[i]==e[0] and d[i+1]==e[1] and d[i+2]==e[2]):
					count+=1
				else:
					continue
			s=s+count
		if(count==0):
			print "NOT FOUND"
		else:
			print search," Is  Found ",s,"times" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> end of case5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	
	elif(choice==6):
		f=open("list.txt","r")
		a=f.read()
		b=a.split()
		for i in b:
			fn=open(i,"r")
			c=fn.read()
			print i," >>>>>>>>>   \n",c
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> end of case6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<	
	elif(choice==7):
		print "Thank u....."
		i=7
	else:
		print "INVALID OPTION..... \n"
		print "Press 0 for details"
	
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> END <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		
	

		
			
			
		
		

	
