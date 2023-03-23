ch = input("Please Enter Your Own Character : ")

if(ord(ch) >= 48 and ord(ch) <= 57): 
    print("The Given Character ", ch, "is a Digit") 
elif((ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122)):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is a Special Character")