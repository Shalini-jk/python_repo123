a = input(("Enter the string which want to check \n"))
new_string = a[::-1]
if(a==new_string):
    print(a)
    print(new_string)
    print("The string is palindrome string")
else:
    print(a)
    print(new_string)
    print("The string is not a palindrome string")