#if else statement in python 

#1)write a python program to check wherther the number is positive, negative or zero.
num1 = int(input("Enter your number: "))

if num1 > 0:
    print("the number is postive. ")
elif num1 < 0:
    print("the number is Neagtive. ")
else:
    print("the number is zero. ")

#2)wriet a python program to check whether the number is even or odd.
num2 = int(input("Enter your number: "))

if num2 % 2 == 0:
    print("the number is even. ")
else:
    print("the number is odd. ")
    
#3)write a python program to check wheather the person is pass or fail. (pass marks ids 40).
marks = int(input("Enter your marks: "))
     
if marks >=  40:
    print("you are pass. ")
else:
    print("you are fail. ")

#4)write a python program to check whether the person is eligible for movie ticket.
age = int(input("Enter your age: "))

if age >= 12 and age <= 17:
    print("free ticket. ")
elif age >= 17 and age <= 59:
    print("Child ticket. ")
elif age >= 59 and age <=60:
    print("Adult ticket. ")
else:
    print("Senior Citizen Ticket. ")