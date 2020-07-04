'''
Default Constructor declaration

def __init__():    

Overloaded Constructor declaaration
def __init__(arg1, arg2, arg3):
    
'''
# Simple Example - 

class employee:
       
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.empCount += 1
    
    def displayCount(self):
        print ("Total number of employees "  + employee.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)


emp1 = employee("Patt", 2000)
emp2 = employee("Matt", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print ("Total number of employees " + str(employee.empCount))
