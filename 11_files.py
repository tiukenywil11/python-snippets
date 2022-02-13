# Python functions for creating, reading, updating, and deleting files

# Opens a file, creates a file if it does not exist
myFile = open('file_sample/myfile.txt','w')

# Get some information from the file
print("Get infromation regarding the file")
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Name: ', myFile.mode)

# Write information to file
print('Adding lines to file_sample/myfile.txt')
myFile.write('I love Python')
myFile.write(' and JavaScript')
print('Closing file for write')
myFile.close()

# Append to file, does not delete previous file content
print('Adding lines to file_sample/myfile.txt without deleting previous file content')
myFile = open('file_sample/myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from a file
print("Opens a file for read, in this instance gets the first 100 characters")
myFile = open('file_sample/myfile.txt', 'r+')
text = myFile.read(100)
print(text)