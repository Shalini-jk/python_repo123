''' here we declare the variable a, b globably so that we can use these variable anywhere in the program
in the given program  we try to implement inheritance.

here we create a class named Shapes which is a base class and the class rectangle and square is a derived class ie child class
here in this program we create an object of derived class(child class)  and access the method of child class as well as base class also
this is what the inheritance means.'''

a = int(input("Enter the value of Length :  "))
b = int(input("Enter the value of breadth :  "))

class Shapes:
    
  def information():
    print("enter the value of length and breadth \n")
    print("now with the help of the length and breadth, find the area and perimeter of rectangle and square")
        
class rectangle(Shapes):
    def area():
      arearec = a * b 
      print("The area  of rectangle is :  ", arearec)
      
    def perimeter():
      peri =  2 * (a + b)
      print(" The perimeter of rectangle is : ", peri)
      
class Square(rectangle):
    def get_area():
        area1 = a * a 
        print("The area of  Square is: ", area1)
        
    def get_perimeter():
        peri1 = 4 * a
        print("The perimeter of Square is : ", peri1)

        
obj = Square
obj.information()
obj.get_area()
obj.get_perimeter()
obj.area()
obj.perimeter()



    
    
        

    
    
    
    
    
    
    
    