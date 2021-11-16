# cube.py
# 
# Computes the cubing of odd numbers and print cube
# If number even, just print number
#
# Written by Evan

def cb(x):
    return x**3

for x in range(0, 19+1):
    if x % 2 == 0:
        print '{} Even and not Cubed'.format(x)
    else:
        print '{} Odd and Cubed'.format(cb(x))
