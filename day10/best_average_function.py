def average(a,b,c):
    return (a+b+c)/3
av1 = average(20,13,17)
av2 = average(17,17,19)
av3 = average(14,14,20)
averages = [av1, av2, av3]

stu1 = "Mehr"
stu2 = "Ali"
stu3= "Babak"
students = ["Mehr", "Ali", "Babak"]

students_average = [(stu1, av1), (stu2,av2), (stu3,av3)]

best_student = None
highest_average = -1

for name, average in students_average:
    #name = student[0]
    #average = student[1]

    if average > highest_average:
        highest_average = average
        best_student = name
print("best student:", best_student)
print("average:", highest_average)