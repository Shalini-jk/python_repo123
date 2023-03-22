First_List = [4,7,8,9,0,6,2]
Second_List = [1,2,3]
First_List.sort()
Second_List.sort()


if First_List == Second_List:
    print("the first list and second list is same ")
else:
    print("the first list and second list is not same")
    
    
l1 = [10, 20, 30, 40, 50]
l2 = [50, 10, 30, 20, 40]

a = set(l1)
b = set(l2)

if a == b:
    print("Lists l1 and l2 are equal")
else:
    print("Lists l1 and l2 are not equal")