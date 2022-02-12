# A function is a block of code, that runs when it's called

# Create a function
def sayHello(name):
    print(f'Hello {name}')

# Call a function, passing parameter 'John Doe'
print("Calling function sayHello:")
sayHello('John Doe')

# Create a function with a return value
def getSum(num1, num2):
    total = num1 + num2
    return total

print("Call a function and assign getSum, with a return value, to a variable")
num = getSum(3, 4)
print(num)


# A lambda function is a small anonymous function, can take any number od arguments, but only have one expression
print("Output of getSum with lambda function format: ")
getSum_lambda = lambda num1, num2: num1 + num2
print(getSum_lambda(10,3))
