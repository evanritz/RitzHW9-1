# square.py
#
# This script takes no arguments 
# Computes the square of the range 0 to 19
# Prints out the squares
#
# Written by Evan

def sq(x):
    return x**2

print "Squares of the range 0 to 19"
for x in range(0, 19+1):
    print "{}^2={}".format(x, sq(x))
