students = {
    "Ali": {
        "economics": 18,
        "math": 17,
        "english": 20,
        "statistics": 19
    },

    "Sara": {
        "economics": 15,
        "math": 14,
        "english": 16,
        "statistics": 17
    },

    "Reza": {
        "economics": 20,
        "math": 19,
        "english": 18,
        "statistics": 20
    },

    "Maryam": {
        "economics": 17,
        "math": 18,
        "english": 16,
        "statistics": 18
    },

    "Amir": {
        "economics": 13,
        "math": 15,
        "english": 14,
        "statistics": 12
    },

    "Niloofar": {
        "economics": 19,
        "math": 20,
        "english": 18,
        "statistics": 19
    },

    "Parsa": {
        "economics": 16,
        "math": 17,
        "english": 15,
        "statistics": 16
    },

    "Yasaman": {
        "economics": 18,
        "math": 19,
        "english": 17,
        "statistics": 20
    }
}

def calculate_average(students):
    average_list = []
    for name, info in students.items():
        average = (info["economics"]+info["math"]+info["english"]+info["statistics"])/4
        average_list.append((name, average))
    return average_list

def find_best_student(students):
    best_student = None
    highest_average = -1
    average = calculate_average(students)
    for name, avg in average:
        if avg > highest_average:
            highest_average = avg
            best_student = name
    return best_student, highest_average

def find_worst_student(students):
    worst_student = None
    lowest_average = 9999
    average = calculate_average(students)
    for name, avg in average:
        if avg < lowest_average:
            lowest_average = avg
            worst_student = name
    return worst_student, lowest_average

def counting_better_students(students):
    count = 0
    average = calculate_average(students)
    for name, avg in average:
        if avg > 17:
            count += 1
    return count

def counting_statistics_upperthan18(students):
    count = 0 
    for name, info in students.items():
        if info["statistics"] > 17:
            count += 1
    return count

def students_report(students):
    average = calculate_average(students)
    for name, avg in average:
        print(f"{name} : {avg}")

def main():
    average = calculate_average(students)
    best = find_best_student(students)
    worst = find_worst_student(students)
    top_students = counting_better_students(students)
    better_statistics_students = counting_statistics_upperthan18(students)
    students_report(students)
    print("students average:", average)
    print("best student:", best)
    print("worst student:", worst)
    print("your excellent students:", top_students)
    print("your top statistics students:", better_statistics_students)
main()
