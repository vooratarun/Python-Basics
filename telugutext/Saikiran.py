#defining a Function To search . . . .
def _Sai(_File,_Str,_Results):
	a=open(_File,"r")
	b,_List,count_1=a.readlines(),[],0	#Assigning . 
	#Main Logic. .(Looping)
	for _lines in range(len(b)):
		c=b[_lines].split()
		for ele in range(len(c)-len(_Str)-1):
			count_2=0
			for kiran in range(len(_Str)):	
				if c[ele]==_Str[kiran]:
					count_2+=1
				ele+=1
			if count_2==len(_Str):
				count_1+=1	#Increment
				_List+=[_lines+1]	#Adding to alist . .
	if count_1!=0:
		_Results[_File]=_List	#Adding to Dictionary (_Results[Keys]=Values)
	return count_1,_Results		#Returning Count and Dictionary . 

#Starting  . . . .(File Operations . )
a=open("list.txt","r")
b=a.read()
c=b.split()
print "To search string in given file list.txt"
String=raw_input("Enter any string to search :: \t")
String_2,TotalCount,Total,Dict=String.split(),0,0,{}	#Assigning . .
print "\nSearch Results : : : \n\n"
for d in c:
	Total,Dict=_Sai(d,String_2,Dict)	#Calling Main function . .
	TotalCount+=Total		#Incresing count
#Printing results present in a Dictionary .
for _ResulT in Dict:
	print "\nIn ",_ResulT,"\tIn Lines :::",Dict[_ResulT]
print "\nTotal Search results about ::: ",String," :::is",TotalCount,"\n"
