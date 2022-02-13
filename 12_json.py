# JSON is commonlu used with data APIs. We can now parse JSON into Python dictionary

# Initialize a sample JSON
import json
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse JSON into dictionary format
print("Parsing a JSON formatted string into dictionary format")
user = json.loads(userJSON)
print(user)
print(user['first_name'])

# Initialize a python dictionary
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

# Parse dictionary format into JSON
print("Parsing dictionary format into a JSON formatted string")
carJSON = json.dumps(car)
print(carJSON)