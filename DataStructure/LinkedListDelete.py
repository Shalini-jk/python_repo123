class node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

node1 = node('elem1')

head = node1

node2 = node('elem2')
node3 = node('elem3')
node4 = node('elem4')
node5 = node('elem5')

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

pointer = head

# deletion of node from middle and end of the Linkedlist ie from any position from the linked list

nodeToBeDeleted='elem2'
while pointer:
    if pointer.next.value == nodeToBeDeleted:
        pointer.next=pointer.next.next
        break
    else:
        pointer=pointer.next
        
        
pointer = head

while(pointer!=None):
    print(pointer.value)
    pointer=pointer.next

