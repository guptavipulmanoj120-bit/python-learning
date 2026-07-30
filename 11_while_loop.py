# while loop

# Question 1: Print numbers from 1 to 10

count = 1

while count <= 10:
    print(count)
    count += 1


# Question 2: Print numbers from 10 to 1


count = 10

while count >= 1:
    print(count)
    count -= 1


# Question 3: Multiplication Table

table = int(input("Enter a number: "))

count = 1

while count <= 10:
    print(table, "x", count, "=", table * count)
    count += 1


# Question 4: Print Even Numbers (1 to 20)

count = 1

while count <= 20:
    if count % 2 == 0:
        print(count)
    count += 1


# Question 5: Keep Taking Input Until User Enters 0


num = -1

while num != 0:
    num = int(input("Enter a number: "))

    if num != 0:
        print("You entered:", num)
    else:
        print("Program Ended!")