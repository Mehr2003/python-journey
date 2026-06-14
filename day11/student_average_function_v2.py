students =(("Mehr", 16, 18, 20), ("Amin", 12, 15, 18), ("Sepehr", 12, 18, 16))
(stu1, stu2, stu3) = students
#print(students)

def calculate_average(economics, math, english):
        return (economics + math + english)/3

best_student = None
highest_average = -1

for name, economics, math, english in students:
    avg = calculate_average(economics, math, english)
    if avg > highest_average:
        highest_average = avg
        best_student = name
print("best student:", best_student)
print("average:", highest_average)