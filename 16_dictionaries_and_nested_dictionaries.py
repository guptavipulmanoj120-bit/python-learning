# Python Dictionaries
# Topics:
# - Dictionary access
# - get()
# - Adding and updating values
# - Deleting values
# - Dictionary loops
# - items()
# - isinstance()
# - Nested dictionaries
# - Filtering dictionary data


# Basic dictionary

student = {
    "name": "Vipul",
    "age": 22,
    "city": "Mumbai",
    "course": "Python"
}

print(student.get("name"))
print(student.get("course", "Python"))

student["age"] = 22
student["course"] = "Python"

del student["city"]

print(student)


# Dictionary loop - keys

student = {
    "name": "Vipul",
    "age": 22,
    "city": "Mumbai",
    "course": "Python",
    "marks": 85
}

for key in student:
    print(key)


# Dictionary loop - values

for key in student:
    print(student[key])


# Dictionary loop - keys and values

for key, value in student.items():
    print(key, "=", value)


# Filter integer values

for key, value in student.items():
    if isinstance(value, int):
        print(value)


# Filter integer key-value pairs

for key, value in student.items():
    if isinstance(value, int):
        print(key, "=", value)


# Nested dictionaries

students = {
    "student1": {
        "name": "vipul",
        "age": 22,
        "city": "mumbai"
    },
    "student2": {
        "name": "rahul",
        "age": 21,
        "city": "Delhi"
    }
}

print(students["student1"]["city"])
print(students["student2"]["name"])

students["student2"]["age"] = 22

students["student1"]["course"] = "python"
students["student2"]["course"] = "python"

print(students)


# Loop through nested dictionaries

for key, student in students.items():
    print(student["name"], "-", student["age"])


# Filter nested dictionary data

students = {
    "student1": {
        "name": "vipul",
        "age": 22,
        "marks": 85
    },
    "student2": {
        "name": "rahul",
        "age": 21,
        "marks": 72
    },
    "student3": {
        "name": "aman",
        "age": 22,
        "marks": 91
    }
}

for key, student in students.items():
    if student["age"] == 22 and student["marks"] > 80:
        print(student["name"])