# If/ Else statements decides if an action within it gets executed or not based on the conditions, if it is true or false

# Comparison operator (==, !=, >, <, >=, <=)

# Simple if statement
x_if = 10
y_if = 5

print('Using simple if statement')
if x_if > y_if:
    print(f'{x_if} is greater than {y_if}')

# If-else statement
x_else = 10
y_else = 50

print('Using if-else statement')
if x_else > y_else:
    print(f'{x_else} is greater than {y_else}')
else:
    print(f'{y_else} is greater than {x_else}')

# Else-if statement
x_elif = 10
y_elif = 10

print('Using else-if statement')
if x_elif > y_elif:
    print(f'{x_elif} is greater than {y_elif}')
elif x_elif == y_elif:
    print(f'{x_elif} is equal to {y_elif}')
else:
    print(f'{y_elif} is greater than {x_elif}')

# Nested if statement
x_nested = 10
y_nested = 10

print('Using nested if statements')
if x_nested > 2:
    if x_nested <= 10:
        print(f'{x_nested} is greater than2 and less than equal to 10')

# Logical operators (and, or, not): used to combine multiple conditional statements

# Using "and" operator (both conditions must be true)
x_and = 10

print('Using "and" statements')
if x_and >2 and x_and <= 10:
    print(f'{x_and} is greater than and less than equal to 10')

# Using "or" operator (only one condition must be true)
x_or = 10

print('Using "or" statements')
if x_or >2 and x_or <= 10:
    print(f'{x_or} is greater than or less than equal to 10')

# Using "not" operator (will proceed if the condition is not equals)
x_not = 10
y_not = 20

print('Using "not" statements')
if not(x_not == y_not):
    print(f'{x_not} is not equal to {y_not}')


# Membership operators (not, not in): used to check if a value is present in an object (lists, sets, tuples, dictionaries)

# Using "in" condition
numbers_in = [1,2,3,4,5]
x_in = 3

print('Using "in" operator to check if "x" is in "numbers" list')
if x_in in numbers_in:
    print(x_in in numbers_in)

    
# Using "not in" condition
numbers_not_in = [1,2,3,4,5]
x_not_in = 13

print('Using "not in" operator to check if "x" is not in "numbers" list')
if x_not_in not in numbers_not_in:
    print(x_not_in not in numbers_not_in)


# Identity operators (is, is not): Compare the objects if they are the same object, with the same memory allocation (different from being just equal)

# Using "is" condition
x_is = 10
y_is = 10

print('Using "is" operator to check if "x" is the same object as "y"')
if x_is is y_is:
    print(x_is is y_is)

# Using "is not" condition
x_is_not = 10
y_is_not = 20

print('Using "is not" operator to check if "x" is not the same object as "y"')
if x_is_not is not y_is_not:
    print(x_is_not is not y_is_not)