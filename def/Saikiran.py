#defining a Function To search . . . .
def Sai(File,Str,Results):
	a=open(File,"r")
	b,List,count1=a.readlines(),[],0	#Assigning . 
	#Main Logic. .(Looping)
	for lines in range(len(b)):
		c=b[lines].split()
		for ele in range(len(c)-len(Str)-1):
			count2=0
			for kiran in range(len(Str)):	
				if c[ele]==Str[kiran]:
					count2+=1
				ele+=1
			if count2==len(Str):
				count1+=1	#Increment
				List+=[lines+1]	#Adding to alist . .
	if count1!=0:
		Results[File]=List	#Adding to Dictionary (Results[Keys]=Values)
	return count1,Results		#Returning Count and Dictionary . 

#Starting  . . . .(File Operations . )
a=open("list.txt","r")
b=a.read()
c=b.split()
print "To search string in given file list.txt"
String=raw_input("Enter any string to search :: \t")
String2,TC,Total,Dict=String.split(),0,0,{}	#Assigning . .
print "\nSearch Results : : : \n\n"
for d in c:
	Total,Dict=Sai(d,String2,Dict)	#Calling Main function . .
	TC+=Total		#Incresing count
#Printing results present in a Dictionary .
for ResulT in Dict:
	print "\nIn ",ResulT,"\tIn Lines :::",Dict[ResulT]
print "\nTotal Search results about ::: ",String," :::is",TC,"\n"
