students = {
    "Ali": {
        "economics": 18,
        "math": 17,
        "english": 20
    },

    "Sara": {
        "economics": 15,
        "math": 14,
        "english": 16
    },

    "Reza": {
        "economics": 20,
        "math": 19,
        "english": 18
    },

    "Maryam": {
        "economics": 17,
        "math": 18,
        "english": 16
    },

    "Amir": {
        "economics": 13,
        "math": 15,
        "english": 14
    }
}

def students_average(students):
    average_list = []
    for name, grade in students.items():
        average = (grade["economics"] + grade["math"] + grade["english"])/3
        average_list.append((name, average))
    return average_list

def find_best_student(students):
    best_student = None
    highest_average = -1
    average = students_average(students)
    for name, avg in average:
        if avg > highest_average:
            highest_average = avg
            best_student = name
    return best_student, highest_average

def find_worst_student(students):
    worst_student = None
    lowest_average = 9999
    average = students_average(students)
    for name, avg in average:
        if avg < lowest_average:
            lowest_average = avg
            worst_student = name
    return worst_student, lowest_average

def find_better_students(students):
    count = 0
    average = students_average(students)
    for name, avg in average:
        if avg > 17:
            count += 1
    return count

def main():
    averages = students_average(students)
    best = find_best_student(students)
    worst = find_worst_student(students)
    better = find_better_students(students)
    print("students & their averages:", averages)
    print("best student:", best[0])
    print("average of best student:", best[1])
    print("worst student:", worst[0])
    print("average of worst student:", worst[1])
    print("upper than 17 students:", better)
main()

    


