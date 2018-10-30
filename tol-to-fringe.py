#!/usr/bin/python

# Program to calculate fringes given a tolerance. 


import math 
#import pyperclip

print(
        '''
        Please Provide Information for the lens:

        1. Radius
        2. Clear Aperature
        3. Given Tolerance
        '''
        )

# Normal Input:
radius = float(input('Radius?'))
ca =  float(input('Clear Aperature?'))
# Three Decimal places for the given tolerance seems to work fine.  
tol = float(input('Tolerance?'))

# wavelength:
'''  Can change this if necessary, though it's 
     almost universally 633nm because that's how the 
     zygo machines' lasers come configured.
'''
w = 633

# perform calculations:
res = (tol * 1e6 * (2 * abs(radius) - math.sqrt(4 * radius**2 - ca**2))) / (abs(radius) * w)
# print output:
res = round(res, 2)
print(res)
input()
#pyperclip.copy(round(res, 2))
