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

def deposit (depositAmt):
    currentBalance = finalAccountBalance + depositAmt
    return currentBalance

def withdraw (withdrawAmt):
    currentBalance = finalAccountBalance - withdrawAmt
    return currentBalance

def checkBal ():
    return finalAccountBalance



restartProcess = "Y"

while(restartProcess == "Y"):
    print("Enter the name of Acc. holder - ")
    accName = input()                               # input() vs raw_input() - Only applicable in Python 2.x versions -
                                                    # input may convert the inpput data from string to suitable format
                                                    # whereas raw_input always takes input in for of string

    print("Enter the Acc. number - ")
    accNum = int(input())

    print("Enter starting balance amount - ")
    finalAccountBalance = float(input())

    print("Enter D for deposting.")
    print("Enter W for withdrawing.")
    print("Enter B for checking balance.")

    print("Select the action you want to perform - ")
    action = str(input())

    if (action == "D" or action == "d"):
        print("How much do you want to deposit ?")
        depositAmt = float(input())
        finalAccountBalance = deposit(depositAmt)
        print ("Amount present in account "+ str(accNum) + " after deposting is - " + str(finalAccountBalance))
        exit
    
    elif (action == "W" or action == "w"):
        withdrawAmt = float (input ("How much would you like to withdraw ?"))
        finalAccountBalance = withdraw(withdrawAmt)
        print ("Amount present in account "+ str(accNum) + " after withdraw is - " + str(finalAccountBalance))
        exit

    elif (action == "B" or action == "b"):
        balance = checkBal ()
        print ("Amount present in account "+ str(accNum) + "  is - " + str(finalAccountBalance))
        exit

    else:
        print("Wrong Choice !!!")

    print("Do you still want to try again ? Enter Y for Yes.")
    restartProcess = input()




    