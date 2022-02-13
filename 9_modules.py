# A module is a file with a set of functions that can be included in your application. There are pre-made modules that can be installed using "pip package manager"

# Importing a core python module
print ("Using datetime module's date.today function")
import datetime

today = datetime.date.today()
print(today)

# Can also import only specific functions from a method (in this case daate function from time datetime)
print ("Using function date imported from method datetime, then calling today function")
from datetime import date

today_from = date.today()
print(today)

# Import method time
print ("Using time module's time function")
import time

timestamp = time.time()
print(timestamp)

# Import only specific functions from a method (in this case time function from time method)
print ("Using function time imported from method time")
from time import time

timestamp = time()
print(timestamp)

# Install modules using pip install manager

print("Install camelcase custom module, then import and use")
# pip install camelcase (This will install camelcase to your system)
# pip freeze (to check list of installed modules)
from camelcase import CamelCase
 
c = CamelCase()
print(c.hump('hello there world'))

# Import custom module, created the python file (custom_module.py)
print('Created a custom module, then called it to this python file')
import custom_module 
from custom_module import validate_email

email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')
