x = input("Enter any string: \n ")
a = x.split()  #use split method to split at whitespaces
a.reverse() #reverse all the elements of the string 
print(' '.join(a))  #concatenate them into a string
