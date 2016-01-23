a="a"
b="b"
c="c"
if cmp(a,b)== -1 and cmp(a,c)== -1 :
	if cmp(b,c)==-1  :
		print a,b,c
elif cmp(b,a)==-1 and cmp(b,c)==-1 :
	if cmp(a,c)==-1:
		print b,a,c
elif cmp(b,c)==-1 and cmp(b,a)==-1:
	print b
	if cmp(c,a)==-1 :
		print b,c,a
