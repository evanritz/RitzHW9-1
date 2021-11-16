# function.py
#
# This script takes no arguments
# Computes the function f(x) = x^2 + 2 over the range 0 to 9
# Prints out f(x) and x
#
# Written by Evan

print "f(x) = x^2 + 2 over the range 0 to 9"
print
for x in range(0, 9+1):
    f_x = x**2 + 2
    print "f(x)={} x={}".format(f_x, x)


