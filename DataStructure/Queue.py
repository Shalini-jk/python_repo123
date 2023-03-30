# queue works on first in first out principle(fifo)

class Queue:
    def __init__( self ):
        self. items = []

    def isEmpty (self):
        return self. items == []

    def enqueue (self, item):
        self. items. insert ( 0, item )

    def dequeue (self):
        return self. items. pop()

    def size (self):
        return len (self.items)
    
q=Queue ()
q.isEmpty ()
q.enqueue ("animals")
q.enqueue ("dog")
q.enqueue ("Elephant")
q.enqueue ("Rabbit")
q.enqueue ("Deer")
q.enqueue ("Snake")

print ("The size of the Queue Before deleting item from Queue :  ", q.size())
q. dequeue()
print ("The size of the Queue after deleting one item from Queue :   ", q.size())

