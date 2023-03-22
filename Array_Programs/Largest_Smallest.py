array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,23,15,17,19]
n= len(array1) 
largest = array1[0]
smallest = array1[0]
for i in range(n):
    if array1[i]>largest:
        largest = array1[i]
    if array1[i]<smallest:
        smallest = array1[i]
print("the largest element in array is: \n",largest)
print("the smallest element in array is: \n",smallest)