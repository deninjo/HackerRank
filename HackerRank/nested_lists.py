# n = int(input("How many elements: "))
'''
records = [["Chi", 20],["Beta", 30],["Alpha", 50]]
for x in records:
    print(x)

print()
print(records[1])
print()
print(records[2][0])
print(len(records))
'''




'''
Given the names and grades for each student in a class of n students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
Example
The ordered list of scores is , so the second lowest score is . 
There are two students with that score: . Ordered alphabetically, the names are printed as:
'''


students = []
for _ in range(int(input("How many students: "))):
    name = input("Name: ")
    grade = float(input("Grade: "))
    students.append([name, grade])


# Sort the students list by grades (second element of each sublist)
students.sort(key=lambda x: x[1])

# Extract the second-lowest grade
second_lowest_grade = None
second_lowest_students = []

# To find the second-lowest grade, we need to handle edge cases where there might be duplicates
if len(students) > 1:
    lowest_grade = students[0][1]
    for student in students:
        if student[1] > lowest_grade:
            second_lowest_grade = student[1]
            break

# Collect all students with the second-lowest grade
for student in students:
    if student[1] == second_lowest_grade:
        second_lowest_students.append(student[0])

# Sort the names of the students with the second-lowest grade
second_lowest_students.sort()

# Print each student's name on a new line
for name in second_lowest_students:
    print(name)

print()
print(students)



