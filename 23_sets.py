# sets 

#Create this list numbers = [10, 20, 10, 30, 20, 40, 30] Convert it into a set and store it in:

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = set(numbers)

print(unique_numbers)

#Now let's practice converting Given names = ["Vipul", "Rahul", "Vipul", "Aman", "Rahul", "Riya"] Create a set called using the set() function

names = ["Vipul", "Rahul", "Vipul", "Aman", "Rahul", "Riya"]

unique_names = set(names)

print(unique_names)

#Start with numbers = {10, 20, 30} Add 40 using the correct set method.

number1 = {10,20,30}

number1.add(40)

print(number1)

# Set + Loop Use a for loop to print every number.

number2 = {10,20,30,40,50}

for number in number2:
    print(number)