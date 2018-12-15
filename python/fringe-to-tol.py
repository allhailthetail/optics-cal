#!/usr/bin/python

# Program to calculate tolerances for lens radii.  


import math 
#import pyperclip

print(
        '''
        Please Provide Information for the lens:

        1. Radius
        2. Clear Aperature
        3. Fringe callout
        '''
        )

# Normal Input:
radius = float(input('Radius?'))
ca =  float(input('Clear Aperature?'))
fringe = float(input('Fringes?'))

# wavelength:
'''  Can change this if necessary, though it's 
     almost universally 633nm because that's how the 
     zygo machines' lasers come configured.
'''
w = 633

# perform calculations:
res = float((fringe * abs(radius) * w) / ((2 * abs(radius) - math.sqrt(4 * radius**2 - ca**2))) * 10e-7)

# print output:
'''
To keep python from automatically rounding 'up' to the 3rd decimal place:
    1. Round to 4 decimal places
    2. Convert to String, 'text'
    3. Delete the 4th decimal place
    4. Convert that string BACK to a float.  

    Workaround, but it works and seems stable.  :)
'''
res = str(round(res, 4))
#this line doesn't seem to be necessary...
#res = res[:-1]
res = float(res)

print(res)
input()
#pyperclip.copy(round(res, 3))
