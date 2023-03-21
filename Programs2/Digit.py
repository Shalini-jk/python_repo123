n = int(input("Enter the value of a:\n"))
sum = 0 ;
while(n != 0):
    a = n % 10
    sum = sum + a
    n = n // 10
print("the sum of all the digit of a number is",sum)