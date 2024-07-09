'''
The provided code stub will read in a dictionary
containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided,
showing 2 places after the decimal.
'''

n = int(input("How many people: "))
student_marks = {}
for _ in range(n):
    name, *line = input("Enter name and marks separated by a white space: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores

for key, value in student_marks.items():
    print(key, ':', value)

query_name = input("Enter query name: ")


if query_name in student_marks:
    scores = student_marks[query_name]
    avg = sum(scores)/len(scores)
    print(round(avg, 2))
else:
    print("Student not found")
