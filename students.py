import csv

students = []

#using csv module to read the csv file and create a list of dictionaries

with open("students.csv") as file:
    reader = csv.DictReader(file, fieldnames=["name", "town",])
    for row in reader:
        students.append(row)




# used when csv has single comma as a separator 
"""    for line in f:
        name, town = line.rstrip().split(",")
        student = {"name": name, "town": town}
        students.append(student)
"""

for student in sorted(students, key=lambda student: student["town"]):
    print(f"{student['name']} is from {student['town']}")