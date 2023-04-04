''' in the given program i am  trying to calculate the simple interest by taking amount , rate and time
as input. here i am trying to raise an exception when the rate of interest is more than 5% 

'''
amount = int (input("Enter the amount : "))
rate = int (input("Enter the rate of interest : "))
time = int(input("Enter the time for how much you want to take :"))
try:
    if rate > 5:
        raise (ValueError(rate)) # here i raised an exception of value and error when the input amount of rate is more than the value given in condition
    interest = (amount * time * rate) / 100
    print('The Simple Interest is', interest)

except ValueError:
    print('interest rate is out of range , rate must be less than 10 %', rate) # here with the help of except i am trying to catch the exception which is raised by try block
    
    