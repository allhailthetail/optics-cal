#!/usr/bin/python

'''
This program will automatically create Job Boss material codes 
when given user input.  
'''

# define main sting:
code = ['   ','  ','  ','  ',' ','     ','  ']

'''
code[0] -- Start Part, First Side, Second Side
code[1] -- Centering and Coating Callout
code[2] -- Coating Machine, if needed
code[3] -- Achromat Callout 
code[4] -- Mandatory Spacing
code[5] -- Coating Number
code[6] -- Double-sided coat 
'''

# begin material entry:

print(
        '''
        Please define how this part is made:

        1. Full Plano
        2. Full CNC
        3. Plano SIDE 1 THEN CNC
        4. Achromat

        '''
        )

entry = int(input('How is it Made?'))

if entry == 1:
    code[0] = 'PPP'
elif entry == 2:
    code[0] = 'CCC'
elif entry == 3:
    code[0] = 'PPC'
elif entry == 4:
    code[0] = 'M  '
    code[3] = 'AC'

# begin coating/centering 

print(
        '''
        1. Coat Only 
        2. Coated and THEN centered 
        3. Centered and THEN coated
        4. Center Only
        5. N/A
    '''
        )

entry = int(input('coated or centered?'))

if entry == 1:
    code[1] = 'B '
elif entry == 2:
    code[1] = 'BA'
elif entry == 3:
    code[1] = 'AB'
elif entry == 4:
    code[1] = 'A '
elif entry == 5:
    code[1] = '  '

# Loop for iff part has a coating...

if entry < 4:
    coatid = ''
    coatmach = ''
    dbl_yn = ''
    print(
            '''
            Please Define Coating Information:
            '''
            )

    code[5] = str(input('Coating ID:'))
    print(coatid)

    code[2] = str(input('Coating Machine:'))
    
    print('Is this part double-side coated?')
    dbl_yn = input('double-side? ')
    if dbl_yn == 'y':
        code[6] = '-2'
    if dbl_yn == 'n':
        code[6] = ' '
            

# prepare code for print, copy, etc.  
code = ''.join(code).upper()
print(code)
input()

