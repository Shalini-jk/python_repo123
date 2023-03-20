a = int(input("enter the first number \n"))
b = int (input("enter the second number \n"))
c = int (input("enter the third number \n"))
if (a>b) and (a>c):
    print(a,"the First value is greatest among all")
elif(b>a) and (b>c):
    print(b," the Second value is greatest among all ")
else:
    print(c,"the third value is greatest among all")