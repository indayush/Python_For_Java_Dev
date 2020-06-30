'''
Types of Loops - 
* While
* For i in Range(value)
* For i in Range(start value, end value)

Noteworthy points are about the resetting value behavior or 'i' variable in different loop systems

'''

import math                                                             # importing math library to use mathrmatical functions

inputNumber = int(input("Enter a number - "))
startCounter = int(input("Enter starting point - "))
endCounter = int(input("Enter ending point - "))
i = 10                                                           # Here i = 10 definition is necessary to set loop start counter
tempStart = startCounter
tempI = i



print()                                                          # for next line
print("Using While - ")
print(startCounter + "\t\t\t" + "Number" + "\t\t\t" + "Square Root\t\t\t" + "Cube Root")          # Different ways to use \t - (Tabspace) in print statement

while (startCounter <= endCounter):
    
    squareRoot = math.sqrt(inputNumber)                            # Here by default, the var type is float cuz of math library
    cubeRoot = math.pow(inputNumber,1/3)                           # we can type cast to get data type of our choice
    
    print(inputNumber , "\t\t\t" , squareRoot, "\t\t\t" , cubeRoot)
    startCounter = startCounter + 1





print()
print("Using For i in Range(value)- ")
print( "Value of i \t\t\t"+ "Square" + "\t\t\t" + "Square Root\t\t\t" + "Cube Root")          
                                                                   
                                                        # The value of i will be reset to 0 if used in for loop in this syntax
for i in range (endCounter):                            # it is equivalent to for(i=0;i<endCounter;i++)
    #squareRoot = math.sqrt(inputNumber)                            
    cubeRoot = math.pow(inputNumber,1/3)
    print(i,"\t\t\t",inputNumber * inputNumber , "\t\t\t" , squareRoot, "\t\t\t" , cubeRoot)





print()
print("Using For i in Range(start value, end value)- ")
print("Value of i " + "\t\t\t" + "startCounter" + "\t\t\t" +"Number" + "\t\t\t" + "Square\t\t\t" + "Cube")          # Different ways to use \t - (Tabspace) in print statement
#for i in range (startCounter,endCounter):                    # This fails as value of startCounter is already more 
                                                              # than endCounter due to while loop. Thus used Temp variable


startCounter = tempStart                                           # Reset values to original  
i = tempI                                                         # Reset values to original  
for i in range (startCounter,endCounter):                                                             
    print(i + "\t\t\t" + startCounter + inputNumber , "\t\t\t" , inputNumber * inputNumber, "\t\t\t" , inputNumber * inputNumber * inputNumber)

# it is equivalent to for(i=startCounter;i<=endCounter;i++)