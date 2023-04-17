''' here we declare the variable a, b globably so that we can use these variable anywhere in the program
in the given program  we try to implement inheritance.
'''
'''here we implement polymorphism. polymorphism means method name in child class is same as method name in parenet class 
ie. the method defined in  parent class and child class is off same name here area and perimeter have same naame 
but defined differently  in child class and parent class '''

a = int(input("Enter the value of Length :  "))
b = int(input("Enter the value of breadth :  "))

class get_Shapes:
    
  def area():
    print("enter the value of length and breadth \n")
    
  def perimeter():
    print("now with the help of the length and breadth, find the area and perimeter of rectangle and square")
        
class rectangle:
    def area():
      arearec = a * b 
      print("The area  of rectangle is :  ", arearec)
      
    def perimeter():
      peri =  2 * (a + b)
      print(" The perimeter of rectangle is : ", peri)
      
      
obj = rectangle
obj.area()
obj.perimeter()
obj1 = get_Shapes
obj1.area()
obj1.perimeter()

    
    
    
        

    
    
    
    
    
    
    
    