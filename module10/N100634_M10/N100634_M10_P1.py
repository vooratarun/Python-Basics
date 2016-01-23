se=raw_input("Enter a sentence: ")# input.
L=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']#Taking all vowels in a list.
print "The total vowels present in Sentece are:- "
d={}#empty list.
for i in L:#taking for loop.
    c=0
    for j in se:# it takes each char in the sentence
           if i==j:
               c=c+1
               d[i]=c   # append to a list
    print i,"\t",c,"times"#printing howmany times the char repeated
print "The dictionary which consists of all chars present in the sentence is:- \n",d#printing the list.
