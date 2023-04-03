'''here first we import the class file to use the methods of that class . we saved that class file with the name 
module.py , hence we import that class file with import module.'''
import Module

# here we create an object for the class which is defined in that class file.

obj = Module.Calculation() 
print("Please select which of the following arithematic operation you want me to perform-\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")  # here we give the choice to the user to perform the calculation according to their need

operation = int(input("1 ,2 ,3 , 4 : \n" )) 

# in the given code we access different method of class file accoding to the different choice entered by the user
 
if operation == 1 :
    Module.addition()
    
elif operation == 2:
    Module.substraction()
    
elif operation == 3 :
    Module.multiplication()
    
elif operation == 4 :
    Module.division()
    
else:
    print("Invalid  input, Please input valid input for appropriate output")

