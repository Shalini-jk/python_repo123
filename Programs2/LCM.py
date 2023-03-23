first_value =  int(input("enter the first number: \n"))
Second_value = int(input("enter the second number: \n"))
for i in range(max(first_value, Second_value), 1 + (first_value * Second_value)):
    if i % first_value == i % Second_value == 0:
        lcm = i
        break
print("LCM of", first_value, "and", Second_value, "is", lcm)