Student_name = ["kavya","samayra","nisha","Abhishek","Keshav",2,5,8,9,4,6]
print (Student_name)
new_index = int(input("Enter the index which you want to remove from the  List: \n"))
del(Student_name[new_index]) # using delete function (it remove by index)
print(Student_name)

new_name= input("Enter the name which you want to remove from the  List: \n")
Student_name.remove(new_name)  # using remove function( it remove by value)
print(Student_name)

new_index = int(input("Enter the index which you want to remove from the  List: \n"))
Student_name.pop(new_index) # using pop punction (it remove by index)
print(Student_name)

Student_name.clear() # it clear the complete list
print(Student_name)




