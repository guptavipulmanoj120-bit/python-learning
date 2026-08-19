#Write a function called find_highest_student(students) It should take the students list and find the student with the highest marks.

student1 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]


def find_highest_student(student1):
    highest = 0
    highest_student = ""

    for student in student1:
        if student["marks"] > highest:
           highest = student["marks"]
           highest_student = student["name"]

    print(highest_student, "=", highest)


find_highest_student(student1)

#write a funcation called find_lowest_student(students) It should take the students list and find the student with the lowest marks.

student2 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]


def find_lowest_student(student2):
    lowest = student2[0]["marks"]
    lowest_student = student2[0]["name"]

    for student in student2:
        if student["marks"] < lowest:
            lowest = student["marks"]
            lowest_student = student["name"]

    print(lowest_student, "=" ,lowest)


find_lowest_student(student2)

# write a function called calculate_average_student(students) It should take the students list and find the average marks of all students.

student3 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

def calculate_average(student3):
    total = 0

    for student in student3:
        total = total + student["marks"]

    average = total / len(student3)
    print("average", "=" ,average)


calculate_average(student3)

# write a funcation called find_highest_student(students) Using the same students list, calculate the average marks automatically without hardcoding 3

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

    print(highest_student, "=" ,highest)

    if highest >= 40:
        print("status = passed")
    else:
        print("status = failed")

find_highest_student(student4)