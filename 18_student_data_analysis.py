#Find the student with the highest marks.

student1 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91},
]

highest = 0
highest_student = ""

for student in student1:
    if student["marks"] > highest:
        highest = student["marks"]
        highest_student = student["name"]

print(highest_student, "=", highest)

#Find the student with the highest marks and print:

student2 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91},
    {"name": "Riya", "age": 20, "marks": 95}
]

highest = 0
highest_student = ""

for student in student2:
    if student["marks"] > highest:
        highest = student["marks"]
        highest_student = student["name"]

print(highest_student, "=", highest)

#Write the code to get the lowest marks and name.

student3 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91},
    {"name": "Riya", "age": 20, "marks": 95}
]

lowest = student3[0]["marks"]
lowest_student = student3[0]["name"]

for student in student3:
    if student["marks"] < lowest:
        lowest = student["marks"]
        lowest_student = student["name"]

print(lowest_student, "=" ,lowest)

#Find the average marks, then print the names of students who scored ABOVE the average.

student4 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91},
    {"name": "Riya", "age": 20, "marks": 95}
]


total = 0

for student in student4:
    total = total + student["marks"]

average = total / len(student4)

print("average","=",average)

for student in student4:
    if student["marks"] > average:
        print(student["name"])


#Find the student with the highest marks, but this time:
#Find the highest marks.
#Print the student's name and marks.
#Also print whether they are "Passed" or "Failed"

student5 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91},
    {"name": "Riya", "age": 20, "marks": 95}
]

highest = 0
highest_student = ""

for student in student5:
    if student["marks"] > highest:
        highest = student["marks"]
        highest_student = student["name"]

print(highest_student, "=", highest)

if highest >= 40:
    print("Status = Passed")
else:
    print("Status = Failed")