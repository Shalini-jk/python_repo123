String = input('Enter the string : \n')
count = 0
value = ""
String = String.lower()
for i in String:
    if i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&'or i == '*' or i == '(' or i == i == '-' or i == '+' or i == '=' or i == '_' or i == ':' or i ==';' or i == '<' or i == '>' or i == '/' or i == '?' or i == '" ' :
        #if True
        count+=1
        value = value + i

if count == 0:
    print('No Special Character found')
else:
    print('Total Special Characters are :' + str(count))
    print(value)