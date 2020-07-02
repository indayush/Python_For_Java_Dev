''' Function Syntax -
def functionName (args):
    Function definition for each function must be with 
    common indentation

Also, all funcs must be defined before using i.e. funcs at the top
& their implementations via variabls or methods at the bottom
following the declarations of funcs


To create a global variable - 
global var_name
this should be at the top
'''
global finalAccountBalance

# No args or return for this function
def func1 ():
    print("Inside Func 1")
    
# Single Argument but no return value
def func2 (arg2):
    print("Inside Func 2 with arg - ",arg2)
    
# Single Argument and a return value
def func3 (arg3):
    print("Inside Func 3 with arg - ",arg3)
    print("Squaring & returning value")
    return arg3*arg3    

# Calling Func1
func1()                     # O/P - Inside Func 1

# Calling Func1 in print
print(func1())              
                            # O/P - Inside Func 1
                            # None
                            # "None" is present because print is expecting a return value which is not present. 
                            # Hence None is printed.

func2(5)                    # Error if called without args. 
                            # O/P - Inside Func 2 with arg -  5

func3(5)
                            # Inside Func 3 with arg -  5
                            # Squaring & returning value

print(func3(5))             # Here due to the print statement we are able to get return value. Hence we can say that all functions return some value 
                            # & print calls a function and recieves a return value.
                            # Inside Func 3 with arg -  5
                            # Squaring & returning value 
                            # 25

# Playing with Args - - - - - - - 
# Function Overloading 

def oneDefaultfunc(arg1, arg2 = 10):
    print ("Arg 1 - ", arg1 , " & Arg 2 - ", arg2)
    return arg1*arg2

# Function Overloading
oneDefaultfunc(5)
'''
Here the output is - 
Arg 1 -  5  & Arg 2 -  10

arg2 value is set as 10 by default if we dont pass any value
'''
# Function Overloading
oneDefaultfunc(5,5)
'''
Here the output is - 
Arg 1 -  5  & Arg 2 -  5

arg2 value is now set as 5. Since we have passed a value in args,
The interpreter will override the default value
'''

result1 = oneDefaultfunc(5)
result2 = oneDefaultfunc(5,5)
print("result1 = ",result1," result2 = ",result2)

'''
result1 =  50  result2 =  25
'''

# Behavior with print function

print(oneDefaultfunc(5))
'''
Arg 1 -  5  & Arg 2 -  10
50
'''

print(oneDefaultfunc(5,5))
'''
Arg 1 -  5  & Arg 2 -  5
25
'''

# Function with dynamic multiple arguments
def multi_Args(*args):
    result = 0
    msg = "Final Sum is "

    for x in args:
        result = result + x
        print("In For - ",result)

    #Case 1
    # return ("Final sum is ",result)
    # return "Final sum is ",result
    # o/p returned for above two returns are | ('Final sum is ', 50)

    #Case 2
    msg = msg + str(result)
    return msg
    # o/p returned is | Final sum is 50


multi_Args(5,10,15,20)
'''
o/p - 
5
15
30
50
'''

print('=================================')
print(multi_Args(5,10,15,20))
'''
Outputs in -

Case 1                                                      Case 2
In For -  5                                                 In For -  5                                                 
In For -  15                                                In For -  15                                                 
In For -  30                                                In For -  30
In For -  50                                                In For -  50
('Final sum is ', 50)                                       Final Sum is 50
'''