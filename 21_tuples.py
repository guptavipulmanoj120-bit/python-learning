# tuples

#Create a tuple containing these subjects python, math and machine learining.

subjects = ("python","math","machine learning")

print(subjects[0])

#Create this tuple marks = (85, 72, 91, 35) The first mark The last mark The total number of marks

mark1 = (85, 72, 91, 35)

print(marks[0])

print(marks[3])

print(len(mark1))

#Tuple + Loop marks = (85, 72, 91, 35) Use a for loop to print every mark.

marks = (85, 72, 91, 35)

for mark in marks:
    print(mark)
    
#Slightly harder Let's calculate the total marks using a tuple hen use a for loop to add every mark to total.

marks = (85, 72, 91, 35)

total = 0 

for mark in marks:
    total = total + mark

print(total)

#Tuple Challenge Now let's combine tuple + function + return
#Set total = 0 Loop through the tuple Add all marks Calculate the average Return the average

marks = (85, 72, 91, 35)


def calculate_tuple_average(marks):
    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)

    return average

average = calculate_tuple_average(marks)

print(average)


#Tuple + Condition The function should Create an empty list Loop through marks If the mark is greater than or equal to 40, add it to the list Return the list. 

marks = (85, 72, 91, 35, 48, 30)

def get_passed_marks(marks):
    passed_mark = []

    for mark in marks:
        if mark >= 40:
            passed_mark.append(mark)

    return passed_mark

result = get_passed_marks(marks)
print(result)

#Tuple challenge Now let's make it slightly harder The function should Start with the first mark as the highest Find the highest mark Return the highest mark Loop through the marks.
    
marks = (85, 72, 91, 35, 48, 30)

def get_highest_mark(marks):
    highest = marks[0]

    for mark in marks:
        if mark > highest:
            highest = mark

    return highest

result = get_highest_mark(marks)
print(result)

#Lowest Mark Now let's see if you can reverse the exact same logic

marks = (85, 72, 91, 35, 48, 30)

def get_lowest_mark(marks):
    lowest = marks[0]

    for mark in marks:
        if mark < lowest:
            lowest = mark

    return lowest

result = get_lowest_mark(marks)
print(result)

# Final Tuple Challenge
# The function should:

# Calculate the average.
# Create an empty list.
# Loop through the marks.
# Add marks greater than the average to the list.
# Return the list.

marks = (85, 72, 91, 35, 48, 30)

def get_marks_above_average(marks):
    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)

    marks_above_average = []

    for mark in marks:
        if mark > average:
            marks_above_average.append(mark)

    return average,marks_above_average

result = get_marks_above_average(marks)
print(result)
