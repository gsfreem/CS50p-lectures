import csv

students = []

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for name, house, patronus in reader:
        students.append({'name': name, 'house': house, 'patronuse': patronus})


for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is in {student['house']} and as a[n] {student['patronus']} patronus")

