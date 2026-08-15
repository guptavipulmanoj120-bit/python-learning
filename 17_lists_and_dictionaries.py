# Practiced working with lists containing dictionaries.

# - Accessed dictionaries using list indexes
# - Looped through list of dictionaries
# - Accessed dictionary values inside loops
# - Filtered data using if conditions
# - Used comparison operators
# - Used multiple conditions with and
# - Practiced real-world student data examples

#print the name of index 1.

student0 = [
    {"name": "Vipul", "age": 22},
    {"name": "Rahul", "age": 21}
]

print(student0[1]["name"])

#loop through the list

student1 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

for student in student1:
    print(student["name"])
    
#Write a loop that prints only the ages:

student2 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

for student in student2:
    print(student["age"])
    
#Print only students whose marks are greater than 80:

student3 = [     
    {"name": "Vipul", "age": 22, "marks": 85},     
    {"name": "Rahul", "age": 21, "marks": 72},     
    {"name": "Aman", "age": 22, "marks": 91} 
] 

for student in student3:     
    if student["marks"] > 80:         
        print(student["name"])
        
#Print the name and marks of students whose marks are greater than 80:

student4 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91}
]

for student in student4:
    if student["marks"] > 80:
        print(student["name"],"=", student["marks"])
        
#Print the names of students who are age 22 AND marks greater than 80:

student5 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91},
    {"name": "Riya", "age": 20, "marks": 95}
]

for student in student5:
    if student["age"] == 22 and student["marks"] > 80:
        print(student["name"])
        
#print the name and marks Condition: marks must be greater than 80 Notice that Riya should also appear, even though she's 20.

student6 = [
    {"name": "Vipul", "age": 22, "marks": 85},
    {"name": "Rahul", "age": 21, "marks": 72},
    {"name": "Aman", "age": 22, "marks": 91},
    {"name": "Riya", "age": 20, "marks": 95}
]

for student in student6:
    if student["marks"] > 80:
        print(student["name"],"=", student["marks"])
        

    



    
    