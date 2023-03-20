# fibnocii series
a= int(input("enter first the numbers:\n"))
b=int(input("enter the second number:\n"))
limit=10
for i in range(a,limit):
    c=a+b;
    a=b;
    b=c;
    print(c,end="")
    
    
