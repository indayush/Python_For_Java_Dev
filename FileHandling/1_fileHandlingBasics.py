# Any extra classes are not required to use File Handling Features in python. 
# They are inherently present in it.

    # open() is used to open the file specified in first parameter, 
    # with access provided in second paramenter. 
    # w = write access
    # w+ = write access + create file if it dosen't exist
    # r = read access 
    # a = append access

# Simple usage -
f = open("myName.txt","w")  
f.write("Ayush Adarsh" + "\r\n")

f.writelines("Line 1" + "\r\n")
f.writelines("Line 2" + "\r\n")
f.writelines("Line 3" + "\r\n")
f.writelines("Line 4" + "\r\n")
f.writelines("Line 5" + "\r\n")

f.close


def myFunc():
    f = open("myFile.txt","w+")                                 


    
    # After File opened, writing data into it.
    for i in range (10):
        f.write("This is line " + str(i) + "\r\n")              # \r - Tabsapce, \n - Next Line
    f.close


# appending into file - 
def appendFunc():
    # Creating a new file
    f = open("D:\\sampleFile.txt","w+")
    f.write("Hello")
    f.close

    # If used 'w' instead of 'a', all the previous data will be overwritten
    f = open("D:\\sampleFile.txt","a")
    f.write("(Appended Text  - World - )")
    f.close




# myFunc()
# appendFunc()

# Checking mode of 'f' used previously.

if f.mode == "w":
    f = open("myName.txt","r")
    contents = f.read()
    print (contents)