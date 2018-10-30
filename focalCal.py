#!/usr/bin/python 
# Intro
radii = 0
print(
        '''
        Instructions for this calculator:
        
        This calculator finds solutions for the EFL, BFL, & FFL
        for individual lenses, as well as Achromats.  

        Note:
        You must use 'sign' notation on this calculator.  
        
        Example:
        
        Val:     Val:
        (pos)   (neg)

             ---
            /   \\
           /     \\
           |      |
           |      |
           \      /
            \    /
             ----
         '''
          )


# Query Achromat or single:

feedback = input('is an Achromat or Single: [a/s] ')
if (feedback == 'a' or feedback == 'A'):
    radii = 4
if (feedback == 's' or feedback == 'S'):
    radii = 2

while radii == 2:
    index = float(input('Glass Index: '))
    r1 = float(input('Radius 1: '))
    r2 = float(input('Radius 2: '))
    ct = float(input('Center Thickness: '))

    # generate EFL for one lens:
    efl = ((index + 1) * r1 * r2) / (index * (index * (ct - r1 + r2) - r1 + r2)) 
    # generate BFL for one lens:
    bfl = ((-1) * (index * (ct - r1) - r1) *r2) / (index * (index * (ct - r1 + r2) - r1 + r2)) 
    # generate FFl for one lens:
    ffl = (r1 * (index * (ct + r2) + r2)) / (index * (index * (ct - r1 + r2) - r1 + r2)) 
    # end this loop:
    radii =+ 1
    # round values to appropriate units:
    efl = round(efl, 2)
    bfl = round(bfl, 2)
    ffl = round(ffl, 2)

    # print the values:
    print(str(efl))
    print(str(bfl))
    print(str(ffl))

    # end this loop: 
    radii =+ 1
 
# Focal Lengths For Achromats:
while radii == 4:
    index = float(input('Glass Index lens 1: '))
    r1 = float(input('Radius 1: '))
    r2 = float(input('Radius 2: '))
    ct = float(input('Center Thickness lens 1: '))
    index_2 = float(input('Glass Index lens 2: '))
    r3 = float(input('Radius 3: '))
    r4 = float(input('Radius 4: '))
    ct_2  = float(input('Center Thickness lens 2: '))

    # Achromat Calculations:

    # generate EFL for lens 1 
    efl = ((index + 1) * r1 * r2) / (index * (index * (ct - r1 + r2) - r1 + r2)) 
    # generate BFL for lens 1
    bfl = ((-1) * (index * (ct - r1) - r1) *r2) / (index * (index * (ct - r1 + r2) - r1 + r2)) 
    # generate FFl for lens 1
    ffl = (r1 * (index * (ct + r2) + r2)) / (index * (index * (ct - r1 + r2) - r1 + r2)) 
    
    
    # generate EFL lens 2
    efl_2 = ((index_2 + 1) * r3 * r4) / (index_2 * (index_2 * (ct_2 - r3 + r4) - r3 + r4)) 
    # generate BFL lens 2
    bfl_2 = ((-1) * (index_2 * (ct_2 - r3) - r3) *r4) / (index_2 * (index_2 * (ct_2 - r3 + r4) - r3 + r4)) 
    # generate FFl lens 2
    ffl_2 = (r3 * (index_2 * (ct_2 + r4) + r4)) / (index_2 * (index_2 * (ct_2 - r3 + r4) - r3 + r4)) 
    
    # generate EFL, BFL, FFL Achromat:
    # EFL Works Correctly
    efl_a = (efl * efl_2) / (efl + efl_2 - (efl - bfl + efl_2 - ffl_2)) 
    # BFL Works Correctly
    bfl_a = ((efl_2 * (efl - (efl - bfl + efl_2 - ffl_2))) / ((efl + efl_2 - (efl - bfl + efl_2 - ffl_2)))) + bfl_2 - efl_2
    # FFL Works Correctly
    ffl_a = (ffl) - ((efl**2) / (bfl + ffl_2))

    # print the values:
    print('\n\t Lens #1 Focal Length:')
    print(round(efl, 2))
    print(round(bfl, 2))
    print(round(ffl, 2))
    print('\n\t Lens #1 Focal Length:')
    print(round(efl_2, 2))
    print(round(bfl_2, 2))
    print(round(ffl_2, 2))
    print('\n\t Achromat Focal Lengths:')
    print(round(efl_a, 2))
    print(round(bfl_a, 2))
    print(round(ffl_a, 2))
    # end this loop:
    radii =+ 1

input()

