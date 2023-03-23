ch = input("Please Enter Your Own Character :  \n")

if(ord(ch) >= 48 and ord(ch) <= 57): 
    print("The Given Character ", ch, "is a Digit") 
elif((ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122)):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is a Special Character")
    
# in the above program we find whether the character is of which type and 
# in this program we put all the special character in array  and then traverse the string with array to find 

string = input("Enter the string : \n")
string.split()
count = 0
array ='[@_!#$%^&*()<>?/\|}{~:,./\[]]' 
for i in range(len(string)):
    
    if string[i] in array:
      count = count + 1  
 
print ("Total number of Special Character are :", count)    
if count > 0 :
    print("string Contain Special Character")
else:
    print("string does not contain special character")