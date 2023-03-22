list1 = [2,4,6,8]
list2 = [3,8,7,5,10,12]
list3 = []
list3.append(list1 + list2) 
print (list3)


result = [] 
small_list = len(list1) < len(list2) and list1 or list2

for i in range(0, len(small_list)): 
	result.append(list1[i] + list2[i]) 

print("Resultant list : " + str(result))