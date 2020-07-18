# Operations in Date & Time 
from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta
# Timedelta is a span of time. It is not an individual instant's value but a range which is between two instants. 
# It represents a duration, the difference between two dates or times.


# Note : 
# Was facing problems while importing the timedelta library as it was not being recognised even after coming from suggestions.
# It was rsolved by adding the library in the file prior to this file in the current folder.
# Need to investigate about it.


# Just adding and printing the values by passing into timedelta class
print(timedelta(days=1,hours=6, minutes=10))

# 1 day, 6:10:00

now = datetime.now()
print('Today is - ', now)
print('Today is - ' + str(now))

# Dunno why the extra space.
# Today is -  2020-07-18 20:55:57.692062
# Today is - 2020-07-18 20:55:57.692062

# Adding date & time into today's date --------
# Adding a day
print('Adding a day in Today\'s date will give - ' + str(now + timedelta(days=1)))         # NOTE: alwas days & not day

# Subtracting an hour
print('Subtracting an hour in Today\'s date will give - ' + str(now + timedelta(minutes=-60)))         

# Adding a weeks & 2 days
print('Adding a weeks & 2 days in Today\'s date will give - ' + str(now + timedelta(weeks=1,days=2)))         

'''
Adding a day in Today's date will give - 2020-07-19 20:55:57.692062
Subtracting an hour in Today's date will give - 2020-07-18 19:55:57.692062
Adding a weeks & 2 days in Today's date will give - 2020-07-27 20:55:57.692062
'''

# Another way of formatting & calculating timedelta
# Calculating 1 week ago date
calcValue = datetime.now() + timedelta(weeks=-1)
formattedValue = calcValue.strftime("%A %B %d, %Y")
print(formattedValue)

calcValue = datetime.now() - timedelta(weeks=1)
formattedValue = calcValue.strftime("%A %B %d, %Y")
print(formattedValue)
'''
Saturday July 11, 2020
Saturday July 11, 2020
'''

# Calculating next 1 week date
calcValue = datetime.now() + timedelta(weeks=1)
formattedValue = calcValue.strftime("%A %B %d, %Y")
print(formattedValue)

calcValue = datetime.now() - timedelta(weeks=-1)
formattedValue = calcValue.strftime("%A %B %d, %Y")
print(formattedValue)
'''
Saturday July 25, 2020
Saturday July 25, 2020
'''

# Calculating time span till a particular date,day,time


# Getting today's day 
today = date.today()                    # was getting error here as used .datetime, instead of .date
                                        # So essential to use proper class

# setting mybudday date for this year
myBudday = date(today.year,2,28)
print(myBudday)
print(myBudday.strftime("%A %B %d, %Y"))
'''
2020-02-28
Friday February 28, 2020
'''

# calc differences between two dates
print((myBudday - today).days)
'''
-141
'''
print((today - myBudday).days)
'''
141
'''


# Checking if budday already passed
if today > myBudday:
    print("Birthday already passed for this year %d days ago." %(today - myBudday).days)
    
    # Since budday passed. Therefore adding an year to my budday.
    # To add date/time to an already defined date Obj, use rplace function 
    myBudday = myBudday.replace(year=today.year+1)
    print(myBudday.strftime("%A %B %d, %Y"))
    '''
    Birthday already passed for this year 141 days ago.
    Sunday February 28, 2021
    '''

else:
    print('Brithday will come in %d days' %(myBudday - today).days)


print('Brithday will come in %d days in next year.' %(myBudday - today).days)
'''
Brithday will come in 225 days in next year.
'''

# calc differences between two dates after adding an year
print((myBudday - today).days)
'''
225
'''
print((today - myBudday).days)
'''
-225
'''
