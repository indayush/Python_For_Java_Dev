month = int(input("Enter the month to evaluate no. of days - "))
                                                # Here int type cast is necessary as checkVal gets error as month is int after assigning 
                                                # value and checkVal is string by default. Hence typecast necessary to perform math
checkVal = month % 2

if (month == 2):                                        # if must always have small 'i'. Capital 'I' in If is wrong
    year = int(input("Enter the year - "))
    if (year % 4 == 0) and (year % 100 != 0):
        print ("Leap year, thus 29 days.")
    else:
        print ("Not Leap year, thus 28 days.")
elif (checkVal == 0):
    print ("The month has 30 days.")
else:
    print ("The month has 31 days.")

# Single line if statements

x,y = 10,20
result = "x is less than y STATEMENT 1" if (x<y) else "x is greater than or equal to y STATEMENT 1"
print(result)

x,y = 20,20
print("x is less than y STATEMENT 2" if (x<y) else "x is greater than or equal to y STATEMENT 2")
