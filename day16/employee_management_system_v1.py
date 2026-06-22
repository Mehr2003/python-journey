employees = {
    "Ali": {
        "salary": 1200,
        "age": 25
    },

    "Sara": {
        "salary": 1800,
        "age": 31
    },

    "Reza": {
        "salary": 2200,
        "age": 28
    },

    "Maryam": {
        "salary": 1600,
        "age": 35
    },

    "Amir": {
        "salary": 900,
        "age": 22
    },

    "Niloofar": {
        "salary": 2500,
        "age": 29
    }
}

def employees_average(employees):
    total = 0
    for name, info in employees.items():
        total += info["salary"]
    average = total / len(employees)
    return average 

def find_best_employee(employees):
    best_employee = None
    highest_salary = -1
    for name, info in employees.items():
        if info["salary"] > highest_salary:
            highest_salary = info["salary"]
            best_employee = name
    return best_employee, highest_salary

def find_worst_employee(employees):
    worst_employee = None
    lowest_salary = 9999
    for name, info in employees.items():
        if info["salary"] < lowest_salary:
            lowest_salary = info["salary"]
            worst_employee = name
    return worst_employee, lowest_salary

def find_better_employees(employees):
    count = 0
    for name, info in employees.items():
        if info["salary"] > 1500:
            count += 1
    return count

def employees_report(employees):
    for name, info in employees.items():
        print (f'{name} : {info["salary"]}')

def main():
    salary_average = employees_average(employees)
    best_employee = find_best_employee(employees)
    worst_employee = find_worst_employee(employees)
    better_employees = find_better_employees(employees)
    employees_report(employees)
    print("salary average=", salary_average)
    print("best employee:", best_employee)
    print("worst employee:", worst_employee)
    print("better employees:", better_employees)
main()