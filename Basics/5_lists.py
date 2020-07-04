print("List Introduction - ")
print("")

print("Simple list creation with predefined elements - ")
myList = ['item1','item2','item3','item4']                          # List creation with elements in it.
print("Length of list is - ",  len(myList))                         # Length of List is given by "len(List_Name)"

print("")
print("")
print("Printing List elements - ")                                  # Print like this only if List does not have int elements
for i in range (len(myList)):
        print(myList[i])

print("")
print("")
print("Printing List elements - Part 2")                                  # Print like this only if List does not have int elements
print(myList)

print("")
print("")
print("Adding List elements - ")
myList2 = []                                                        # Empty List creation 
myList2.append("val1")                                              # Adding items into List                                                                   
myList2.append("val2")
myList2.append("val3")
myList2.append("val4")

for i in myList2:
        print(i)

print("")
print("")
print("Removing List elements - ")
myList2.remove("val2")                                              # Removing item by Name from List     

for i in myList2:
        print(i)

print("")
print("")
print("Pushing List elements - ")
myList2.append("val2")                                              # Adding items into List. This will be added at LAST position.
for i in myList2:
        print(i)

print("")
print("")
print("Inserting elements at a specific index in List - ")
myList2.insert(1,"VAL_NEWLY_Inserted")
for i in myList2:
        print(i)

print("")
print("")
print("Deleting by Index List elements - ")
del myList2[1]                                                      # Removing item by Index from List    
for i in myList2:
        print(i)

print("")
print("")
print("Bulk/Range Deleting by Index List elements - ")
del myList2[0:1]                                                    # Bulk Remove items by Index from List (from index 0-1)    
for i in myList2:
        print(i)

print("")
print("")
print("Dynamic insertion into List - ")
myList3 = []
i = 1
maxCount = 10
for counter in range (maxCount):        
        myList3.append(i) 
        i= i + 1

for i in myList3:
        print(i)

print("")
print("Max value in list is - ", max(myList3))

print("")
print("Min value in list is - ", min(myList3))

print("")
valueToFind = 7
print("Finding no. of occurances of value - ", valueToFind)
print("Frequency of value ", valueToFind ," in the list is - ", myList3.count(valueToFind))                     


myList3.append(7)
myList3.append(7)
myList3.append(4)
myList3.append(2)
myList3.append(11)
myList3.append(-5)


print("")
valueToFind = 7
print("Finding no. of occurances of value - ", valueToFind)
print("Frequency of value ", valueToFind ," in the list is - ", myList3.count(valueToFind))                     

print("")
print("Final List is - ")
#for i in range(len(myList3)):
print(myList3)