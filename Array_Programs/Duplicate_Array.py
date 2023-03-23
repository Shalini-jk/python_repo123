arr = [1, 2, 3, 4, 2, 7, 8, 3, 7, 5, 1, 8];     
print("Duplicate elements in given array: ");    
#Searches for duplicate element    
for i in range(0, len(arr)): # here we go to each element from begining
    for j in range(i+1, len(arr)): # here we go toeach elemewnt after the first index
     if(arr[i] == arr[j]):
         print(arr[j]);  