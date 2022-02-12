# This is a comment

'''
This is a multiline comment
or docstring (used to define a functions purpose)
'''

"""
Alternative multiline comment
"""

'''
- Variables are case sensitive 
- Must start with a letter or an underscore
- Can have numbers, but cannot start with one
'''

# int
x = 1

#float
y = 2.5

#str
name = 'John'

#bool
is_cool = True

print('Printing initialized variables:')
print(x,y,name,is_cool)

# Multiple assinment
x_mult, y_mult, name_mult, is_cool_mult = (1, 2.5, 'John', True)

print('Printing multiple assigned variables:')
print(x_mult,y_mult,name_mult,is_cool_mult)

# Basic math
print('Basic math x + y =')
a = x + y
print(a)

# Type of variable
print('Check type of varible for "x"')
print(x,type(x))

# Casting
# Changes variable 'x' type int to str
print('Parse variable "x" from int to str')
print(x,type(x))
x = str(x)
print(x,type(x))

# Changes variable 'y' type float to int (removing decimal)
print('Parse variable "y" from float to int')
print(y,type(y))
y = int(y)
print(y,type(y))

# Changes variable 'y' back to float (adding decimal)
print('Parse variable "y" back to float')
z = float(y)
print(y,type(y))
print(z,type(z))
