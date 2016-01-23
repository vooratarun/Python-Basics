#Change dictionary keys to values, values to keys.

d={"abc":1,"bcd":2,"def":3} # dictionary
a=d.keys()  # keys 
b=d.values()  # values 
d2=dict(zip(b,a))                    # zip the values as keys and keys as values
print "reverse dictionary is",d2  # printing dictionary
