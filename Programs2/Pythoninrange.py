First_value = int(input ("Please, Enter the Lowest Range Value:\n "))  
last_value = int(input ("Please, Enter the Upper Range Value: \n "))  
  
print ("The Prime Numbers in the range are: ")  
for a in range (First_value, last_value + 1):  
    if a > 1:  
        for i in range (2, a):  
            if (a % i) == 0:  
                break  
        else:  
            print (a)