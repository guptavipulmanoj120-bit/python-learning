#Change Aman’s marks from 91 to 95 using a loop.

student0 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

for student in student0:
    if student["name"] == "Aman":
        student["marks"] = 95
        
#let's combine finding + updating + adding Challenge Find Rahul and Change his marks to 80 Add a new key:

student1 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

for student in student1:
    if student["name"] == "Rahul":
        student["marks"] = 80

print(student)

#Find Rahul, then Change his marks from 72 → 80 Add "course": "Python" Print Rahul's complete dictionary:

student2 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

for student in student2:
    if student["name"] == "Rahul":
        student["marks"] = 80
        student["course"] = "Python"
        print(student)
        
#Now don't find Rahul Find every student whose marks are greater than 80 and add "status": "Passed" Then print the complete dictionaries:

student3 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

for student in student3:
    if student["marks"] > 80:
        student["status"] = "passed" 
        print(student)

#Using the same students list, add "status": "Passed" to every student 
# with marks greater than 80, then print the entire students list after 
# the loop This time, don't print inside the if.

student4 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

for student in student4:
    if student["marks"] > 80:
        student["status"] = "Passed"

print(student4)

#Update + Filter Change the "status" based on marks marks > 80 → "Passed" marks <= 80 → "Failed" Then print the entire students list Then print the entire students list.
        
student5 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

for student in student5:
    if student["marks"] > 80:
        student["status"] = "Passed"
    else:
        student["status"] = "failed"

print(student5)

#Create a variable Then use a loop to calculate the total marks of all students.

student6 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

total = 0

for student in student6:
    total = total + student["marks"]

print(total)

#There are 3 students Calculate the average marks and print it

student7 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

total = 0

for student in student7:
    total = total + student["marks"]

average = total / 3

print(average)

#Using the same students list, calculate the average marks automatically without hardcoding 3

student8 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

total = 0

for student in student8:
    total = total + student["marks"]

average = total / len(student8)

print(average)
