students = (("Mahr", 18), ("Ali", 16), ("Amin", 20))
print(students)

best_student = None
highest_average = -1

for name, average in students:
    if average > highest_average:
        highest_average = average
        best_student = name
print("best student:", best_student)
print("average:", highest_average)