# Python Lists - Basics
# Topics:
# - Creating Lists
# - Indexing
# - Negative Indexing
# - Updating Items
# - List Methods


# Question 1: Create and Print a List


fruits = ["Apple", "Mango", "Banana", "Orange"]

print(fruits)


# Question 2: Print the First Item

print(fruits[0])


# Question 3: Print the Last Item

print(fruits[3])


# Question 4: Update an Item
# Change "Mango" to "Grapes"


fruits[1] = "Grapes"

print(fruits)


# Question 5: Negative Indexing

print(fruits[-1])


# Question 6: Add an Item Using append()


fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)


# Question 7: Insert an Item

fruits = ["Apple", "Banana", "Orange"]

fruits.insert(1, "Mango")

print(fruits)


# Question 8: Remove an Item

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)


# Boss Challenge

numbers = [10, 20, 30, 40, 50]

# Print original list
print(numbers)

# Print first number
print(numbers[0])

# Print last number using negative indexing
print(numbers[-1])

# Change 30 to 35
numbers[2] = 35

# Add 60 to the end
numbers.append(60)

# Insert 15 at index 1
numbers.insert(1, 15)

# Remove 40
numbers.remove(40)

# Print final list
print(numbers)