# Find the highest marks among a list of student dictionaries with the use of return 

student1 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]
def find_highest_student(student1):
    highest = 0

    for student in student1:
        if student["marks"] > highest:
            highest = student["marks"]

    return highest

result = find_highest_student(student1)
print(result)

#print the name of student with the heighest marks with the use return

student2 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]
def find_highest_student(student2):
    highest = 0
    highest_student = ""

    for student in student2:
        if student["marks"] > highest:
            highest = student["marks"]
            highest_student = student["name"]

    return  highest_student,highest

result = find_highest_student(student2)
print(result)

# find the highest marks among a list of student dictionaries with the use of return and also print the status of student whether he is passed or failed

student3 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]
def find_highest_student(student3):
    highest = 0
    highest_student = ""

    for student in student3:
        if student["marks"] > highest:
            highest = student["marks"]
            highest_student = student["name"]

    if highest >= 40:
        print("status = passed")
    else:
        print("status = failed")

    return  highest_student,highest

result = find_highest_student(student3)
print(result)

#

student4 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

def find_highest_student(student4):
    highest = 0
    highest_student = ""

    for student in student4:
        if student["marks"] > highest:
            highest = student["marks"]
            highest_student = student["name"]

    if highest >= 40:
        status = "passed"
    else:
        status = "failed"

    return  highest_student,highest,status


student_name, marks, status = find_highest_student(student4)

print(student_name, "=", marks)
print("Status =", status)

# Challenge 1 — Get Passed Students

student5 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91},
    {"name": "Riya", "age": 20, "marks": 35}
]

def get_passed_student5(student5):
    passed_student5 = []

    for student in student5:
        if student["marks"] >= 40:
            passed_student5.append(student["name"])


    return passed_student5

result = get_passed_students(student5)
print(result)

#Instead of returning only the names, return the complete student dictionaries for students who passed.

student6 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91},
    {"name": "Riya", "age": 20, "marks": 35}
]

def get_passed_students(student6):
    passed_student6 = []

    for student in student6:
        if student["marks"] >= 40:
            passed_students.append(student)


    return passed_student6

result = get_passed_students(student6)
print(result)

#Calculate the average marks Create an empty list Add the complete student dictionary if their marks are above the average Return that list.

student7 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91},
    {"name": "Riya", "age": 20, "marks": 35}
]

def get_students_above_average(student7):
    total = 0

    for student in student7:
        total = total + student["marks"]

    average = total / len(student7)

    students_above_average = []

    for student in student7:
        if student["marks"] > average:
            students_above_average.append(student)

    return students_above_average

result = get_students_above_average(student7)
print(result)

#nstead of hardcoding 80, the function should accept the marks as an argument.

student8 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91},
    {"name": "Riya", "age": 20, "marks": 35}
]

def get_students_above_marks(student8, minimum_marks):
    result = []

    for student in student8:
        if student["marks"] > minimum_marks:
            result.append(student)

    return result

result = get_students_above_marks(student8,80)

for student in result:
    print(student["name"])



