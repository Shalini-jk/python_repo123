num1 = 16 # for integer
print(num1, 'is of type', type(num1))

num2 = 9.0 # for float(decimal)
print(num2, 'is of type', type(num2))

num3 = 4+2j # for complex
print(num3, 'is of type', type(num3))

num4 = "shalini joshi" # for string
print(num4, 'is of type', type(num4))

num4 = 9+2.8 # combination of float or integer results float vale
print(num4, 'is of type', type(num4))


 # creating the list ( list can be modified as it is dynamic)
 
items = ["car" , "bike" ,"Cycle",45]   
collections=["grocery","cosmetics","breverage"]

# accessing the items from list by providing the index with the list name
print (items[2])
print (items[1])
print (items[3])
print (collections[2])

# creating the tuple ( tuple cannot be modified as it is static)

stocks=("laptop", "keyboard", "mouse","printers",209,"406.89")

# accessing the items from the tuple by their index

print (stocks[2])
print (stocks[0])
print (stocks[1])
print (stocks[3])
print (stocks[4])
print (stocks[5])

# creating set datatype

Roll_No ={111,112,113,114,115,116,117}
Student_Name={"shalini","keshav","nisha","raj","saloni","aliya","pragya"}

print(Roll_No)
print(Student_Name)

# creating Dictionary datatype

foods ={'Breverage':'Orange Juice, Soft drink , Coke', 'Starter':'Paneer Chilli , Muffin', 'Main Course':'Chapati and paneer k sabji, chole Kulche'}

print(foods['Breverage'])
print(foods['Main Course'])
print (foods['Starter'])

m,n,p=6,7,9
print(m,n,p)