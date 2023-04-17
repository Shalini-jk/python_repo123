a = int(input("Enter the value of Length :  "))
b = int(input("Enter the value of breadth :  "))

class Shapes1:
    
  def area():
      arearec = a * b 
      print("The area  of rectangle is :  ", arearec)
      
  def perimeter():
      peri =  2 * (a + b)
      print(" The perimeter of rectangle is : ", peri)
        

    
      
obj = Shapes1
obj.area()