"""
 decimal to : bin,oct,hex
"""


## enter decimal input
input_x = 1234
## return binary representation
print(f'input_x in binary form is : {bin(input_x)}')
## or
print('input_x in binary form is : ',format(input_x,'b'))
##  return octal representation
print(f'input_x in octal form is : {oct(input_x)}')
## or
print('input_x in octal form is : ',format(input_x,'o'))
## return hexadecimal representation
print(f'input_x in hex form is : {hex(input_x)}')
## or
print('input_x in hex form is : ',format(input_x,'x'))

"""
 bin,oct,hex to decimal
"""
input_bin = '0b10011010010'
input_hex = '4d2'
input_oct = '2322'

list_of_inputs = [input_bin,input_hex,input_oct]
dividers = [2,16,8]
"""
bin to decimal = int(number,2)
oct to decimal = int(number,8)
hex to decimal = int(number,16)

"""

for input,divider in zip(list_of_inputs,dividers):
    
    print(f'{input} to decimal gives : ',int(input,divider))