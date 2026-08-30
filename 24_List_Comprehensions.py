# list comprehensions

#Given this list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] reate a new list containing only the even numbers using list comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [number for number in numbers if number % 2 == 0]

print(result)

#Write a list comprehension that takes and creates a new list containing the squares of only the odd numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = [number * number for number in numbers if number  % 2 != 0]

print(result)

#Create a new list containing the doubled values of numbers greater than 10.

numbers = [2, 5, 8, 11, 14, 17, 20]

result = [number*2 for number in numbers if number > 10]

print(result)

#Write a program to create list and find all the numbers that are even or odd

numbers = [1, 2, 3, 4, 5]

result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print(result)

#Create a new list containing "Big" for numbers >= 20 and "Small" for numbers < 20

numbers = [10, 15, 20, 25]

result = ["Big" if number >= 20 else "Small" for number in numbers]

print(result)

#Create a new list containing the cubes of numbers divisible by 2.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [number*number*number for number in numbers if number % 2 == 0]

print(result)

#Create a new list containing the numbers greater than 10, but multiply each by 3.

numbers = [5, 10, 15, 20, 25, 30]

result = [number * 3 for number in numbers if number > 10]

print(result)

#Create a new list where:
#If the number is even → store its square
#If the number is odd → store its cube

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [number*number if number % 2 == 0 else number*number*number for number in numbers]


print(result)