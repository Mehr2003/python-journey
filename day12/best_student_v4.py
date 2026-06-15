students = (("Amin", 16, 13, 17), ("Mehr", 19, 20, 17), ("Sara", 13, 14, 16))

def stu_avg(economics, math, english):
    return (economics+math+english)/3

best_student = None
highest_average = -1

for name, economics, math, english in students:
    average = stu_avg(economics, math, english)
    if average > highest_average:
        highest_average = average
        best_student = name
print("best student:", best_student)
print("average:", highest_average)
    