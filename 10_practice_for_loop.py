# Question 1: Sum of Numbers

num = int(input("Enter a number: "))

total = 0

for i in range(1, num + 1):
    total = total + i

print("Sum =", total)


# Question 2: Factorial

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)


# Question 3: Count Even and Odd Numbers

num = int(input("Enter a number: "))

even = 0
odd = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even =", even)
print("Odd =", odd)

