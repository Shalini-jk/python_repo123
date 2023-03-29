# stack works on first in last out number (filo) or last in first out principle (lifo)
 
stack_example = []
 
stack_example.append('one')
stack_example.append('two')
stack_example.append('three')
stack_example.append('four')
 
print('Initial stack with 4 elements one, two, three, four loaded in sequence')
print(stack_example)
 
print('3 Elements popped from stack in LIFO order:')
print(stack_example.pop())
print(stack_example.pop())
print(stack_example.pop())
 
print('\nStack after 3 elements are popped:')
print(stack_example)

print('\nStack is left with one element only')
print(stack_example.pop())

