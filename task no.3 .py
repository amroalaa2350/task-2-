student1 = {"name": "Ahmed", "grades": [80, 90, 85]}
student2 = {"name": "Sarah", "grades": [75, 70, 80]}
student3 = {"name": "Laila", "grades": [95, 100, 90]}

students = [student1, student2, student3]

for student in students:
    name = student["name"]
    grades = student["grades"]
    total = grades[0] + grades[1] + grades[2]
    average = total 
    print(name, ":", average)
