'''
Types of Loops - 
* While
* for i in range(value)
* for i in range(start value, end value)

Noteworthy points are about the resetting value behavior or 'i' variable in different loop systems
Also, for range - counter starts from start value and ends before end value, i.e. end value is not included in counting.
e.g. for i in range(5,10) will iterate through - 5,6,7,8,9 & NOT 10
'''

import math                                                             # importing math library to use mathrmatical functions

inputNumber = int(input("Enter a number - "))
startCounter = int(input("Enter starting point - "))
endCounter = int(input("Enter ending point - "))
tempStart = startCounter



print()                                                          # for next line
print("Using While - ")
print("S. No." + "\t\t\t" + "Number" + "\t\t\t" + "Square Root\t\t\t" + "Cube Root")          # Different ways to use \t - (Tabspace) in print statement

while (startCounter <= endCounter):
    
    squareRoot = math.sqrt(inputNumber)                            # Here by default, the var type is float cuz of math library
    cubeRoot = math.pow(inputNumber,1/3)                           # we can type cast to get data type of our choice
    
    print(startCounter, "\t\t\t" ,inputNumber , "\t\t\t" , squareRoot, "\t\t\t" , cubeRoot)
    startCounter = startCounter + 1




# Headers
print()
print("Using For i in Range(value)- ")
print( "Value of i \t\t"+ "Square" + "\t\t\t" + "Square Root\t\t\t" + "Cube Root")          
# Headers

                                                        # The value of i will be reset to 0 if used in for loop in this syntax
for i in range (endCounter):                            # it is equivalent to for(i=0;i<endCounter;i++)
    #squareRoot = math.sqrt(inputNumber)                            
    cubeRoot = math.pow(inputNumber,1/3)
    print(i,"\t\t\t",inputNumber * inputNumber , "\t\t\t" , squareRoot, "\t\t\t" , cubeRoot)




# Headers
print()
print("Using For i in Range(start value, end value) - ")
print("Value of i " + "\t\t" + "Number" + "\t\t\t" + "Square\t\t\t" + "Cube")          # Different ways to use \t - (Tabspace) in print statement
# Headers
#for i in range (startCounter,endCounter):                    # This fails as value of startCounter is already more 
                                                              # than endCounter due to while loop. Thus used Temp variable. 
                                                              # We can also reassign the value but to keep it clea, didn't do so.


startCounter = tempStart                                           # Reset values to original  
i = 0                                                              # Reset values to original  
for i in range (startCounter,endCounter):                                                             
    print(i, "\t\t\t" ,inputNumber,"\t\t\t\t", inputNumber * inputNumber, "\t\t\t" , inputNumber * inputNumber * inputNumber)

# it is equivalent to for(i=startCounter;i<=endCounter;i++)

print()
print()
# Looping over collection of objects is also possible
Days = ["monday","tuesday","wednesday","thursday","friday","saturday"] 
for j in Days:
    print(j)
''' o/p-
monday
tuesday
wednesday
thursday
friday
saturday
'''

# Skipping & Breaking on values in loop
print()
print()
print('=========================================================')    
for i in range (1,10):
    if (i%2==0):
        print (i)
''' o/p-
2
4
6
8
'''


print()
print()
print('=========================================================')    
for i in range (1,10):
    if (i==7):
        break
    else:
        print (i)
''' o/p-
1
2
3
4
5
6
'''


# enumerate function
# Printing index of value in loop as generally python dosn't iterate through a collectionusing index 
print()
print()
print('=========================================================')    
Days = ["monday","tuesday","wednesday","thursday","friday","saturday"] 
for i,j in enumerate(Days):
    print(i, j)

''' o/p-
0 monday
1 tuesday
2 wednesday
3 thursday
4 friday
5 saturday
'''