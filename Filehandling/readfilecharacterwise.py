file = str(input("Enter the name of the file with .txt extension:\n "))
file=open(file,'r')


for line in file:
    for character in line:
        print(character)
        
