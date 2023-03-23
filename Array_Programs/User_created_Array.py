array1 = []  
  
value = int (input (" Enter the total number of the Array elements: "))  

print (" Enter the items into List 1 : ")  
for i in range(1, value + 1):  
    num = int ( input (" Enter the value of %d index is :" %i))  
    array1.append(num) # insert the items into the list1 
print("The newley created list are:\n",array1)
array1.sort()
print("the array after sorting", array1)