#Print the true if both dictionaries having same key and values. Take
#two input dictionaries.

d={}                         # dictionary one
a=input("enter the range to creat the dictionary")
for i in range(a): 
	b=raw_input("enter the key as name")           # taking input keys
	c=input("enter the  value as number")            # taking input values as integers
	d[b]=c                                                             #assing the dictionary
print d
d1={}                   # assigning second dictionary
a=input("enter the range to creat second dictionary")
for i in range(a):
	b=raw_input("enter the key as name")
	c=input("enter the value as number")
	d1[b]=c 
print d1
if d==d1 :                       # checking the two dictionaries if both are same or not
	print "True"      # printing statement as positive
else :
	print "False"   ## printing statement as negitive
