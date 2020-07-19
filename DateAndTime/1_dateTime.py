# Starting with Date & time from python libraries. 
# "datetime" is a python standard module and "date", "time" & "datetime" are libraries within them
# Python importing example - 

import time                                         # Directly importing the library         
from datetime import date                           # Importing library from it's module
from datetime import datetime

# imported timedelta here only because i was unable to import it in the dateTimeOperations.py file
from datetime import timedelta
# Defining Main function
def main():
    
    # Getting today's date -
    todayDate = date.today()
    print(todayDate)                                # O/P - 2020-07-04

    # Getting the components individually -
    print('day = ' , todayDate.day)
    print('month = ' , todayDate.month)
    print('year = ' , todayDate.year)
    

    # Using weekday function (Monday == 0 ... Sunday == 6)
    print('weekday = ' , todayDate.weekday())

    # Using weekday function (Monday == 1 ... Sunday == 7)
    print('ISO weekday = ' , todayDate.isoweekday())
    
    # Using weekday function - 
    days = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
    print("Today's Day is " + days[todayDate.weekday()] )

    # Creating Timestamp by using now() & repplace function
    today = str(datetime.now())
    print(today)

    today = ((today.replace(" ","_").replace(":","_"))).replace('-','_')
    print(today)

    # Creating Timestamp Without Mili-Seconds
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(today)
    today = ((today.replace(" ","_").replace(":","_"))).replace('-','_')
    print(today)

# Calling Main
main()
'''
Outputs -

2020-07-18
day =  18
month =  7
year =  2020
weekday =  5
ISO weekday =  6
Today's Day is Sat
2020-07-18 21:02:07.329019
2020_07_18_21_02_07.329019
2020-07-18 21:02:07
2020_07_18_21_02_07
'''