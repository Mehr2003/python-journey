students = (("Amin", 16, 13, 17), ("Mehr", 19, 20, 17),
("Sara", 13, 14, 16), ("Samin", 15, 16.5, 18))

def stu_avg(economics, math, english):
    average = (economics + math + english)/3
    return average
for name, economics, math, english in students:
    average = stu_avg(economics, math, english)
    result = stu_avg(economics, math, english)
    #print(name, ":", average)

def find_best_student(students):
    best_student = None
    highest_avg = -1
    for name, economics, math, english in students:
        average = stu_avg(economics, math, english)
        if average > highest_avg:
            highest_avg = average
            best_student = name
    return best_student, highest_avg
result = find_best_student(students)
#print("name:", result[0])
#print("average:", result[1])

def find_worst_student(students):
    worst_student = None
    lowest_average = 9999
    for name, economics, math, english in students:
        average = stu_avg(economics, math, english)
        if average < lowest_average:
            lowest_average = average
            worst_student = name
    return worst_student, lowest_average
result = find_worst_student(students)
#print("worst student:", result[0])
#print("average:", result[1])

def main():
    best = find_best_student(students)
    worst = find_worst_student(students)
    print("best:", best)
    print("worst:", worst)
main()
