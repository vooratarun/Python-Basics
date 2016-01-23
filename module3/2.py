f=open("list.txt","r")
b=f.read()
c=b.split()
print "\tfilename\tdata"
print"\t..............\t.............."
for i in c :
	g=open(i,"r")
	h=g.read()
	print "\t",i,"\t\t",h
f.close()
