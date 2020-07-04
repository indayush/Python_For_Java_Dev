# Creating classes & functions within them.
# All members within class must start with same indentation, else we will get error


class myClass():

# self keyword functions like this keyword in java
    def method1(self):
        print ("myClass method1")
    
    def method2(self, someString):
        print ("myClass method2 and arg is - " + someString)


class myClass2():

# self keyword functions like this keyword in java
    def method1(self):
        print ("myClass2 method1")
    
    def method2(self, someString):
        print ("myClass2 method2 and arg is - " + someString)


# To inherit a class or multiple classes, put it's name in the args 
class anotherClass(myClass,myClass2):
    
    def method1(self):
        # Here necessary to put self in args as it will give error when calling while inside another class 
        myClass.method1(self)
        myClass2.method2(self,'Calling from another class')
        print ("anotherClass method1")

    # Here we are using concept of overriding, same emthod name but from different class performing different task
    def method2(self):
        print ("anotherClass method2")
  

def main():
    c = myClass()

    # No argument is sent for self keyword.
    c.method1()
    c.method2('Ayush')

    print('=======================================')

    c2 = anotherClass()
    c2.method1()
    c2.method2()
    
# This executes the main() function only if this file is executed as the main program.
if __name__ == '__main__':
    main()
    
