Student_name = ["kavya","samayra","nisha","Abhishek","Keshav"]
new_name = input("Enter the new name of student:\n")
Student_name.append(new_name)  # using built in append()
print("the newly added student are", Student_name)

new_index = int(input("Enter the index at which you want to add the new name: \n"))
Student_name.insert(new_index,new_name)
print("Updated record according to your choice: \n", Student_name)