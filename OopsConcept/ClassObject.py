a = int (input("Enter the value for first number :  "))
b = int(input("Enter the value of second number :  "))

class Calculation:
    
    def addition():               
        add = a + b
        print ("the addition of two numbers are :", add)
    
    def substraction():
        sub = a -  b
        print ("the subtraction of two numbers are :", sub)  
    
    def multiplication():
        mul = a * b
        print ("the multiplication of two numbers are :", mul) 
    
    def divison():
        if a > b:           
           div = a / b
           print ("the division of two numbers are :", div)  
        else:
            div = b / a
            print ("the division of two numbers are :", div)

obj = Calculation
obj.addition()
obj.substraction()
obj.multiplication()
obj.divison()           
            
            
        
        




