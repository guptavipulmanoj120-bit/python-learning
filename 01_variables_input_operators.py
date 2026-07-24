#Question 1 - Store and Print
name = "Vipul"
age = 21
city = "Mumbai"

print("Name:", name)
print("Age:", age)
print("City:", city)

# Question 2 - Favorite Things
favorite_movie = "Spider-Man"
favorite_programming_language = "Python"
favorite_number = 24

print("\nFavorite Movie:", favorite_movie)
print("Favorite Programming Language:", favorite_programming_language)
print("Favorite Number:", favorite_number)

# Question 3 - Swap Variables
a = 10
b = 20

print("\nBefore Swap")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter Swap")
print("a =", a)
print("b =", b)

# Question 4 - Data Types
print("\nData Types")

print(type("Vipul"))
print(type(21))
print(type(25.5))
print(type(True))

# Question 5 - Personal Information
name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\nHello", name)
print("You are", age, "years old.")
print("You live in", city)

# Question 6 - Favorite Number
favorite_number = int(input("\nEnter your favorite number: "))

print("Your favorite number is:", favorite_number)

# Question 7 - Sum of Two Numbers
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)

# Question 8 - Area of Rectangle
length = int(input("\nEnter length: "))
width = int(input("Enter width: "))

area = length * width

print("Area of Rectangle =", area)

# Question 9 - Area of Circle
radius = int(input("\nEnter radius: "))

area = 3.14 * radius * radius

print("Area of Circle =", area)

# Question 10 - Arithmetic Operators
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("\nAddition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
print("Floor Division =", num1 // num2)
print("Modulus =", num1 % num2)
print("Power =", num1 ** num2)

