students = (
    ("Ali", 18, 17, 20),
    ("Sara", 14, 16, 15),
    ("Reza", 20, 19, 18),
    ("Maryam", 17, 18, 16)
)

def student_avg(economics, math, english):
    average = (economics + math + english)/3
    return average

def find_best_student(students):
    best_student = None
    highest_average = -1
    for name, economics, math, english in students:
        average = student_avg(economics, math, english)
        if average > highest_average:
            highest_average = average
            best_student = name
    return best_student, highest_average
result = find_best_student(students)
print("best student:")
print("name:", result[0])
print("average:", result[1])

def find_worst_student(students):
    worst_student = None
    lowest_average = 9999
    for name, economics, math, english in students:
        average = student_avg(economics, math, english)
        if average < lowest_average:
            lowest_average = average
            worst_student = name
    return worst_student, lowest_average
result = find_worst_student(students)
print("worst student:")
print("name:", result[0])
print("average:", result[1])

def find_good_students(students):
    count = 0
    for name, economics, math, english in students:
        average = student_avg(economics, math, english)
        if average > 17:
            count +=1
    return count
result = find_good_students(students)
print("good students:", result)