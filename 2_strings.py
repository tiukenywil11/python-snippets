# Strings in Python is surrounded by single of double quotes

name = 'Brad'
age = 37

# Concatenate
print('Example output of basic concatenation:')
print('Hello, my name is ' + name + ' and I am '+ str(age))

# String formatting

# Arguments by position
print('Example output of arguments by position:')
print('Hello, my name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (Python 3.6+)
print('Example output of F-Strings:')
print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = 'hello world'

# Capitilize string
print('Using method of str, capitalize:')
print(s.capitalize())

# Make all uppercase
print('Using method of str, upper:')
print(s.upper())

# Make all lower case
print('Using method of str, lower:')
print(s.lower())

# Swap case of upper and lower
print('Using method of str, swap-case:')
print(s.swapcase())

# Gets length
print('Using method of str, len')
print(len(s))

# Replace
print('Using method of str, replace:')
print(s.replace('world', 'everyone'))

# Count a number of a value (This case counts the number of h)
print('Using method of str, count:')
sub = 'h'
print(s.count(sub))

# Starts with: returns true or false depending if string starts with the same value inputted (This case returns true, because string starts with 'hello')
print('Using method of str, startswith:')
print(s.startswith('hello'))

# Ends with: returns true or false depending if string ends with the same value inputted (This case returns true, because string end with 'd')
print('Using method of str, endswith:')
print(s.endswith('d'))

# Splits string into a list
print('Using method of str, split:')
print(s.split())

# Finds first instance of input value's position in string (In this case 'r' is in the 8th position, so returns '8')
print('Using method of str, find:')
print(s.find('r'))

# Is alphanumeric: returns true or false depending if string has both alphabet and numbers (Will return false because of space in string)
print('Using method of str, isalnum:')
print(s.isalnum())

# Is alphabet:returns true or false depending if string has only alphabet (Will return false because of space in string)
print('Using method of str, isalpha:')
print(s.isalpha())

# Is alphanumeric:returns true or false depending if string has only numbers (Will return false because of space in string)
print('Using method of str, isnumeric:')
print(s.isnumeric())