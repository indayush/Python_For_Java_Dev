print("Hi, Please input your name - ")                                              # Cursor goes to the next line. Like println("")
                                                                                    # Not like print("")

name = input()                                                                           # Input syntax - No variable type defined
print("You have provided input as - " + name)                                            # Sting concat syntax


print('Printing Data type of variable name - ', type(name))                                      # Print Data type of variable                                       

print("Hi, Please input your age - ")
age = input()                                                                            # Input syntax - No variable type defined
#print(age)                                                                              # No variable type print

age = int(age)                                       # Type cast to 'int' type & print
#print("int type output - " + age)                   # Can't print string & other data type in one statement like in java
print("int type output - ", age)                     # For multiple data types in single statement, they must be seperated with comma 


age = float(age)                                                                          
print("float type output - ", age)                   # Type cast to 'float' type & print

#height = float(input())
print("Enter your height")
print("Height is - ",float(input()))                 # Type cast & take input inside the print command itself
                                                     # The input is required before the print, so it will seem like the compiler is stuck here


BMI = input(print("Enter your BMI Index - "))        # Here if we execute, the print statement will run before asking the input but, 
print("You have provided input as - " + BMI)         # compiler will  also print "None" becoz no data type defined for variable
                                                     # i.e. - Enter your BMI Index -
                                                     #        None3
                                                     #        You have provided input as - 3


Density = input("Enter your Density Index - ")       # Here if we execute, the print statement will run before asking the input and 
print("You have provided input as - " , Density)     # compiler will "NOT" print None 
                                                     # i.e. - Enter your Density Index - 4


var1 = input('Enter First number - ')
var2 = input('Enter Second number - ')
var3 = var1 + var2
print(var3)                                          # This will concatinate the variables and print them as string
                                                     # To have them functioning as numbers, we need to typecast them while taking input
                                                      

var11 = int(input('Enter First number at int typecasted - '))
var22 = int(input('Enter Second number at int typecasted - '))
var33 = var11 + var22
print(var33)