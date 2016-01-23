#2). Print all the first characters in the string “India is my country”?

a="India is my country"   
b=a.split()  # splitting string to list
print b
for i in b :
	print i[0]  # print first chars in values of list
