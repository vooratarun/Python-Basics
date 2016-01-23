#count the no.of words in given file name
f=open("tarun.txt","r")   #open file
g=f.read()   #read
s=g.split()
print "the no of words in the file  is",len(s) # print
f.close()
