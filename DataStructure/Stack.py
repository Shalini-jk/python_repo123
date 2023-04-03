# stack works on first in last out number (filo) or last in first out principle (lifo)
 
class Stack:
     def __init__ (self):
         self. items = []

     def isEmpty (self):
         return self. items == []

     def push (self, item):
         self. items.append (item)

     def pop (self):
         return self. items.pop()

     def peek (self):
         return self. items [len(self.items)-1]

     def size (self):
         return len (self.items)
     
s = Stack()

print (s. isEmpty())
s.push ("Student")
s.push ("Teacher")
s.push ("Docter")
s.push ("Lawyer")
s.push ("Engineer")
s.push ("Scientist")

print ("getting top element after inserting some elements in the stack:   ", s.peek())

s.push ("Judge")

print ( "Size of the Stack after entering all the element :  ", s.size())
print (" Here we check that still the stack is empty or not after entering all the elements :  ",s.isEmpty())
print ("After pushing one new  element we find the  Peek(top) element :   ", s.peek())

s.push ("Advocate")

print (s.pop())
print (s.pop())
print (" After pop (deleting some items from stack we again get the Top element:  )",s.peek())
print("Total no of items present in stack after performing all the operation:  ", s.size())
