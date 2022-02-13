# A class is a like a blueprint for creating onjects.  An object has properties and methods (functions) associated with it.

# Creating a class
class User:

    # Creating a constructor
    def __init__(self, name):
        self.name = name

# Initialize a user object
print('Initialize a class assigned to "brad" variable, checking type of "brad" ')
brad = User('Brad Traversy')
print(type(brad))

# Creating a class with multiple parameters
class User_multiple_parameters:

    # Creating a constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

print('Initialize a class with multiple parameters assigned to "brad" variable, gets the age of "brad" User only ')
brad_multiple_parameters =  User_multiple_parameters('Brad Traversy', 'brad@gmail.com', 37)
print(brad_multiple_parameters.age)

# Creating a class with methods

class User_methods:

    # Creating a constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

print('Initialize a class with methods assigned to "brad", calls greeeting methods')
brad_methods =  User_methods('Brad Traversy', 'brad@gmail.com', 37)
print(brad_methods.greeting())

print('Calls a method has_birthday to add age to User brad')
brad_methods.has_birthday()
print(brad_methods.greeting())


# Extend a class to reuse all fields of previous class
class Customer(User_methods):

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    # Override method from previous class
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}, and my balance is {self.balance}'

# Initialize an extended class and run greeting
print("Initialize a class Customer which extends User")
janet = Customer('Janet Johnson', 'janel@yahoo.com', 25)
print(janet.greeting())

# Initialize an extended class
print("Initialize a class Customer which extends User, calling a new method on new class")
janet.set_balance(500)
print(janet.greeting())