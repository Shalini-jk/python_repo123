arr = [1, 2,3,4,5,6,7,8,9,10,11,12,13,15,17];
arr.reverse()
print("The elements of array after reversing ",arr)

# now we can do it by swapping the number between the two index
n = len(arr)
start = arr[0]
end = n- 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start = start +  1
    end = end - 1

print("The elements of array after reversing ",arr)
