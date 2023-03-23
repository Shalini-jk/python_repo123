list1 = []  
  
items = int (input (" Enter the total number of the list elements: "))  

print (" Enter the items into List 1 : ")  
for i in range(1, items + 1):  
    num = int ( input (" Enter the value of %d index is :" %i))  
    list1.append(num) # insert the items into the list1 
print("The newley created list are:\n",list1)
     
