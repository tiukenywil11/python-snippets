# A List is a collection which has order, and is changeable. It also allows duplicate members.

# Create list
numbers = [1,2,3,4,5]

print('Display lists initialize normally')
print(numbers)

# Creating a list using a constructor
numbers2 = list((1,2,3,4,5))

print('Display lists initialize using aconstuctor')
print(numbers2)

# Get a value
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Get second value on the list (Oranges)
print('Gets second value of list using "fruits[1]": ')
print(fruits[1])

# Replaces value on the list (Rpelace Oranges to Blueberries)
print('Appends second value "fruits[1]" from Orange to Blueberries')
fruits[1] = 'Blueberries'
print(fruits[1])

# Gers length of list
print('Using a method of list, len:')
print(len(fruits))

# Append to the list (Append Mangos)
print('Append the value "Mango" to the list using "append":' )
fruits.append('Mangos')
print(fruits)

# Remove from the list (Remove Grapes)
print('Remove the value "Grapes" from the list using "remove":' )
fruits.remove('Grapes')
print(fruits)

# Insert value to the list using an index (Strawberries)
print('Insert the value "Strawberries" to index "2" in the list using "insert"')
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove value with an idex from the list using "pop" (Removing Straberries using pop(2))
print('Remove the value from index "2" ("Strawberries") in the list using "pop"')
fruits.pop(2)
print(fruits)

# Reverse the list
print('Using a method of list, reverse:')
fruits.reverse()
print(fruits)

# Sort list alphabetically
print('Using a method of list, sort:')
fruits.sort()
print(fruits)

# Sort list alphabetically
print('Using a method of list, sort, while enabling reverse:')
fruits.sort(reverse=True)
print(fruits)