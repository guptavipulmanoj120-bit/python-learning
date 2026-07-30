# Python For Loop Practice
# Topics: for loop, range(), if condition, nested loop


# Example 1: Print numbers from 0 to 9

for i in range(10):
    print(i)


# Example 2: Print name 5 times

for i in range(5):
    print("Vipul")


# Example 3: Loop through a string

name = "Vipul"

for letter in name:
    print(letter)


# Example 4: Range with step value

for i in range(5, 31, 5):
    print(i)


# Question 1: Multiplication Table

table = int(input("Enter your number: "))

for i in range(1, 11):
    print(table, "x", i, "=", table * i)


# Question 2: Print numbers from 20 to 30

for i in range(20, 31):
    print(i)


# Question 3: Print multiples of 3 from 3 to 30

for i in range(3, 31, 3):
    print(i)


# Question 4: Print name with count

text = "Vipul"

for i in range(1, 11):
    print(i, text)


# Question 5: Print numbers from 1 to user input

num1 = int(input("Enter your number: "))

for i in range(1, num1 + 1):
    print(i)


# Question 6: Reverse counting

num2 = int(input("Enter your number: "))

for i in range(num2, 0, -1):
    print(i)


# Question 7: Odd and Even check

num3 = int(input("Enter your number: "))

for i in range(1, num3 + 1):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")


# Question 8: Fizz Challenge

for i in range(1, 21):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)


# Boss Challenge: Square Pattern

num4 = int(input("Enter number: "))

for i in range(num4):
    for j in range(num4):
        print("*", end="")
    print()
