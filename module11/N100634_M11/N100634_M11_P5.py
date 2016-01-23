# Sort the given dictionary

Z={"cat":5,"apple":1, "ant":2, "bat":3, "ball":4, }   # defining dictionary
a=Z.keys()     # keys as list
b=Z.values()   # values as list
a.sort()           # sorting the keys list  ....it started by taking ASCII values of the strings
b.sort() 	    #	sorting the values list
print b
print a
d=dict(zip(a,b))      # zip the  sorted keys list and values list
print d              # printing the dictionary
