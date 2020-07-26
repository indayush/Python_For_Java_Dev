import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

# Print the name of the OS
print (os.name)
'''
# O/p for os.name on Windows OS is -
nt
'''

# Check for item existence and type
print ("Item exists: " + str(path.exists("myfile.txt")))        # File Name is not case sensitive
print ("Item is a file: " + str(path.isfile("myFile.txt")))
print ("Item is a directory: " + str(path.isdir("myFile.txt")))
'''
Item exists: True
Item is a file: True
Item is a directory: False.
'''

# Absolute File Path
print ("Item's Absolute File path: " + str(path.realpath("textfile.txt")))
# This worked even if file didn't exist


# Splitting file name & the path
print ("Item's path and name: " + str(path.split(path.realpath("textfile.txt"))))

'''
Item's Absolute File path: E:\Python VS\Projects\Python_For_Java_Dev\textfile.txt
Item's path and name: ('E:\Python VS\Projects\Python_For_Java_Dev', 'textfile.txt')
'''

# Get the modification time

t = path.getmtime("textfile.txt")
print (t)
'''
1595788058.8539457
'''

# ctime() is used to convert the time into readable format
# getmtime() is used to get the last modified time
t = time.ctime(path.getmtime("textfile.txt"))
print (t)
'''
Sun Jul 26 23:57:38 2020
'''
print (datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

# Calculate how long ago the item was modified
td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
print ("It has been " + str(td) + " since the file was modified")
print ("Or, " + str(td.total_seconds()) + " seconds")
'''
It has been 0:08:19.750540 since the file was modified
Or, 499.75054 seconds
'''