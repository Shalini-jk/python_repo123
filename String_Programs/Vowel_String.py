String = input('Enter the string : \n')
count = 0
String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        #if True
        count+=1
#check if any vowel found
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))