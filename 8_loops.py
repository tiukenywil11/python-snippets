# "for" loop is used to iterate over a object with sequence (e.g. list, set, tuple, disctionary, string)

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple "for" loop
print('Using a simple "for" loop')
for person in people:
    print(f'Current Person: {person}')

# Using break to end a loop
print('Using a "for" loop with a "break" statement')
for person in people:
    if person == 'Sara':
        break
    print(f'Current Person: {person}')

# Using a continue to skip an interation for the loop
print('Using a "for" loop with a "continue" statement')
for person in people:
    if person == 'Sara':
        continue
    print(f'Current Person: {person}')

# Using range to get a certain range to loop at
print('Using a "for" loop using rannge of people as loop condition')
for i_range in range(len(people)):
    print(people[i_range])

print('Using a "for" loop using rannge of numbers as loop condition')
for i_range in range(0,11):
    print(f'Number: {i_range}')


# "while" loops execute a set of statements as long as a condition remains true

count = 0
print('Using a simple "while" loop')
while count < 10:
    print(f'Count: {count}')
    count += 1