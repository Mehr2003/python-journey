class Student:
    def __init__(self, name, economics, math, english) -> None:
        self.name = name
        self.economics = economics
        self.math = math
        self.english = english
    def calculate_average(self):
        average = (self.economics + self.math + self.english)/3
        return average
    def pass_or_fail(self):
        average = self.calculate_average()
        if average > 17:
            return True
        else:
            return False
    def show_info(self):
        status = "Pass!" if self.pass_or_fail() else "Fail!"
        return f"{self.name} | {self.calculate_average()} | {status}"
    
students = [
    Student("Ali", 18, 17, 20),
    Student("Sara", 15, 14, 16),
    Student("Reza", 20, 19, 18),
    Student("Maryam", 17, 18, 16),
    Student("Amir", 13, 15, 14),
    Student("Niloofar", 19, 20, 18),
    Student("Parsa", 16, 17, 15),
    Student("Yasaman", 18, 19, 17),
    Student("Arman", 14, 13, 15),
    Student("Sahar", 20, 18, 19)
]
def find_best_student(students):
    best_student = None
    highest_average = -1
    for student in students:
        if student.calculate_average() > highest_average:
            highest_average = student.calculate_average()
            best_student = student.name
    return best_student, highest_average
result = find_best_student(students)
print("best student:", result)

def find_worst_student(students):
    worst_student = None
    lowest_average = 9999
    for student in students:
        if student.calculate_average() < lowest_average:
            lowest_average = student.calculate_average()
            worst_student = student.name
    return worst_student, lowest_average
result = find_worst_student(students)
print("worst student:", result)

def students_average(students):
    total = 0
    for student in students:
        total += student.calculate_average()
        average = total / len(students)
    return average
result = students_average(students)
print("class average=", result)

def find_star_students(students):
    count = 0
    for student in students:
        if student.calculate_average() > 17:
            count += 1
    return count
result = find_star_students(students)
print("class stars:", result)

print("information:")
for student in students:
    print(student.show_info())
        