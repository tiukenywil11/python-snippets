# A Dictionary is a collection tha has no order, can be changed, and is indexed. It does not allow duplicate members

# Create dictionary
print('Display dictionary initialized normally:')
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, type(person))

# Use constructor
print('Display disctionary initialized using a constuctor:')
person2 = dict(first_name='Sara', last_name='Williams', age=30)
print(person2, type(person2))

# Get value from dictionary
print('Getting the value "first_name" from "person" dictionary: ')
print(person['first_name'])

# Get value from dictionary using 'get'
print('Getting the value "first_name" from "person" dictionary using "get": ')
print(person.get('last_name'))

# Add key/value pair
print('Adding phone number key/value pair to the dictionary: ')
person['phone'] = '555-555-5555'
print(person)

# Get all dictionary keys
print('Get all keys from the dictionary')
print(person.keys())

# Get all dictionary items, item is a key/value pair in one variable
print('Get all items from the dictionary')
print(person.items())

# Copy a dictionary
print('Copy all key/value pairs from person to person3')
person3 = person.copy()
print(person3)

# Add key/value pair to duplicate dictionary "person3"
print('Adding city key/value pair to the duplicate dictionary "person3": ')
person3['city'] = 'Boston'
print(person3)

# Remove an item from the dictionary
print('Remove age key/value pair from person dictionary using del: ')
del(person['age'])
print(person)

# Remove an item from the dictionary using pop
print('Remove age key/value pair from person dictionary using pop: ')
person.pop('phone')
print(person)

# Clear all key/value pairs from the dictionary (returns an empty dictionary)
print("Clears all key/value pair in the dictionary")
person.clear()
print(person)

# Get length of the dictionary (returns number of key/value pairs)
print("Get length of dictionary person3:")
print(len(person3))

# Create ist of dictionaries
print("Create a list of dictionaries: ")
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 24}
]
print(people)

# Gets specific values from list of dictionaries
# gets people[1] = {'name': 'Kevin', 'age': 24}, then the ['name'] = Kevin
print("Get key/value pairs from index 1, then select the "name" key: ")
print(people[1]['name'])

