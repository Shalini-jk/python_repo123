Student_name = ["kavya","samayra","nisha","Abhishek","Keshav"]
new_list = sorted(Student_name) # arranging elements alphabetically
print("Displaying list before arranging it alphabetically",Student_name)
print("Displaying list after arranging it alphabetically",new_list)

list1 = ["aaaa", "a", "tttt", "aa","b"] # arranging elements by its length also
new_list1 = sorted(list1, key=len)
print("Displaying list before arranging it alphabetically or length wise",list1)
print("Displaying list after arranging it alphabetically or length wise",new_list1)