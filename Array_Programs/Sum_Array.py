array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,23,15,17,19]; 
print("the sum of all elements of an array are as follow:\n",sum(array1)) # using sum function
 # now add all the elements using loop
 
sum1=0
n = len(array1)
for i in range(n):
     sum1 = sum1 + array1[i]
print("the sum of all elements of an array are as follow:\n",sum1) 
    
       