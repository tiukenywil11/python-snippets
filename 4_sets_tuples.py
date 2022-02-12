# A Tuple is a collection which has order, but is not changeable. It also allows duplicate members.

# Create tuple
print('Display tuple initialized normally:')
fruits=  ('Apples','Oranges','Grapes')
print(fruits)

# Creating a tuple using a constructor
print('Display tuple initialized using a constuctor:')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
print(fruits2)

# Showing type tuple
print('Displays how to initialize type tuple properly:')

print('No trailing comma:')
fruits3 = ('Apples')
print(fruits3, type(fruits3))

# Single value tuple needs trailing comma
print('Single value tuple with trailing comma:')
fruits3_tuple = ('Apples',)
print(fruits3_tuple, type(fruits3_tuple))

# Get value of a tuple
# Get second value on the list (Oranges)
print('Gets second value of the tuple using "fruits[1]": ')
print(fruits[1])

# Cant change the value of tuple
# fruits[0] = 'Pears' (Would cause an TypeError: 'tuple' object does not support item assignment)

# Delete tuple
del fruits3
# print (fruits3) (Would cause a NameError: name 'fruits3' is not defined.)

# Gers length of tuplle
print('Using a method of tuple, len:')
print(len(fruits))


# A Set is a collection which has no order, and unindexed. It also does not allow duplicate members.

# Create set
fruits_set  = {'Apples', 'Oranges', 'Mango'}

# Check if value is in a set (returns True or False)
print ('Checks if value "Apples" is in the set "fruits_set"')
print ('Apples' in fruits_set)

# Adding value to set (would be added to random indexes when printed, because set is unindexed)
print('Adding "Grape" to "fruits_set')
fruits_set.add('Grape')
print(fruits_set)

# Removing value from set 
print('Removing "Grape" from "fruits_set')
fruits_set.remove('Grape')
print(fruits_set)

# Clear the set entirely (Empty set will remain)
print('Clear all values from "fruits_set')
fruits_set.clear()
print(fruits_set)

# Delete the whole set
del fruits_set
# print (fruits_set) (Would cause a NameError: name 'fruits_set' is not defined.)
