Array = [5,6,4,2,6,1,9,8,20,7]
arry1 = Array
print(arry1)
for i in range(len(Array)):
    min_indx = i
    
    for j in range(i+1, len(Array)):
    
        if Array[min_indx] > Array[j]:
            min_indx = j

    Array[i], Array[min_indx] = Array[min_indx], Array[i]

print("The sorted array by doing selection sort",Array)

