'''In the given program the variable a , b are declared globally. hence it is known as globale variable
so that we can use these variable all over the program.
'''
a = int (input("Enter the value for first number :  "))
b = int(input("Enter the value of second number :  "))

'''here we make a class in which we make multiple methods and we can 
access this method by creating object of the class  in which these functions are defined'''
class Calculation:             
    ""
      
# explicit function (these function can be called by using the object)
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
            
            
        
        



