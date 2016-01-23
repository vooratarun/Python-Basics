a="abc"
b="abb"
c="aaa"
if len(a)==len(b)and len(b)==len(c):
	if cmp(a,b)==1 and cmp(a,c)==1 :
		if cmp(b,c)==1:
			print c,b,a
	elif cmp(b,c)==-1 and cmp(b,a)==-1 :
		if cmp(c,a)==-1:
			print b
	elif cmp(c,a)==1 and cmp(c,b)==1 :
		if cmp(a,b)==1:
			print b,a,c
	
	



