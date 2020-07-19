import calendar
from datetime import datetime
from datetime import date


textCal = calendar.TextCalendar(calendar.SUNDAY)

# iterate through the days of a month in an year
myObj = textCal.itermonthdates(2020,1)
print(myObj)

# Object reference printed -
'''
<generator object Calendar.itermonthdates at 0x00000160B056C580>
'''

# itermonthdays iterate through the dates in a month
for i in textCal.itermonthdays(2020,1):
    # print(i)
    '''    
        0   - 0 because these dates belong to some other month's date
        0   - zeroes mean that the day of the week is in an overlapping month
        0
        1   - Jan 1, 2020 starting from here
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
        12
        13
        14
        15
        16
        17
        18
        19
        20
        21
        22
        23
        24
        25
        26
        27
        28
        29
        30
        31
        0
    '''

# iterate through the months in an year
for name in calendar.month_name:
    print (name)

    '''
    January
    February
    March
    April
    May
    June
    July
    August
    September
    October
    November
    December
    '''

for name in calendar.day_name:
    print(name)
    
    '''
    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
    Sunday
    '''

# WAP to get all the first fridays in a month for an year

for monthCounter in range (1,13):
    cal = calendar.monthcalendar(2020,monthCounter)

    # The first friday will fall either in first week or second week.
    ''' This is how weeks are stored in a month
    cal[0] returns an array of days of first week

    0:[0, 0, 1, 2, 3, 4, 5]
    1:[6, 7, 8, 9, 10, 11, 12]
    2:[13, 14, 15, 16, 17, 18, 19]
    3:[20, 21, 22, 23, 24, 25, 26]
    4:[27, 28, 29, 30, 31, 0, 0]
    '''
    weekOne = cal[0]
    weekTwo = cal[1]

    # Now we have two weeks of the current month in above variables.
    # We will check if the Friday of these weeks return a date value or 0
    # As, earlier found that, 0 because these dates belong to some other month's date

    ''' Here, was getting error because used Small brackets instead of Box brackets
    if weekOne(calendar.FRIDAY) != 0:
        result = weekOne(calendar.FRIDAY)
    else:
        result = weekTwo(calendar.FRIDAY)
    '''
    if weekOne[calendar.FRIDAY] != 0:
        result = weekOne[calendar.FRIDAY]
    else:
        result = weekTwo[calendar.FRIDAY]

    # print("%10s %2d" %(calendar.month_name[monthCounter],result))
    print("%10s %2d" % (calendar.month_name[monthCounter], result))

    '''
         January  3
        February  7
           March  6
           April  3
             May  1
            June  5
            July  3
          August  7
       September  4
         October  2
        November  6
        December  4
    '''


today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("Tomorrow will be "+days[(today.weekday()+1)%7])   
# print(today.weekday())


print(datetime.date(datetime.now()))
print(date.today())
