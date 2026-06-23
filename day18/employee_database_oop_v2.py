class Employee:
    def __init__(self, name, salary, age) -> None:
        self.name = name
        self.salary = salary
        self.age = age
    def get_salary(self):
        return self.salary
    def is_highesr_than(self):
        if self.salary > 2000:
            return True
        else:
            return False
    def apply_raise(self, percent):
        self.salary = self.salary + (self.salary * (percent/100))
        return self.salary
    def show_info(self):
        status = "Best Employee" if self.is_highesr_than() else "Not Best"
        return f"{self.name} | {self.salary} | {self.age} | {status}"
    
employees_list = [
    Employee("Ali", 1200, 25),
    Employee("Sara", 1800, 31),
    Employee("Reza", 2200, 28),
    Employee("Maryam", 1600, 35),
    Employee("Amir", 900, 22),
    Employee("Niloofar", 2500, 29),
    Employee("Parsa", 1400, 26),
    Employee("Yasaman", 1950, 27),
    Employee("Arman", 1700, 30),
    Employee("Sahar", 2100, 24)
]

def salary_average(employees_list):
    total = 0
    for employee in employees_list:
        total += employee.salary
    average = total / len(employees_list)
    return average
result = salary_average(employees_list)
print("salary average for this company:", result)

def find_best_employee(employees_list):
    best_employee = None
    highest_salary = -1
    for employee in employees_list:
        if employee.salary > highest_salary:
            highest_salary = employee.salary
            best_employee = employee.name
    return best_employee, highest_salary
result = find_best_employee(employees_list)
print("best employee:", result)

def find_worst_employee(employees_list):
    worst_employee = None
    lowest_salary = 9999
    for employee in employees_list:
        if employee.salary < lowest_salary:
            lowest_salary = employee.salary
            worst_employee = employee.name
    return worst_employee, lowest_salary
result = find_worst_employee(employees_list)
print("worst employee:", result)

def counting_better_employees(employees_list):
    count = 0
    for employee in employees_list:
        if employee.salary > 2000:
            count += 1
    return count
result = counting_better_employees(employees_list)
print("better employees:", result)

print("information:")
for employee in employees_list:
    print(employee.show_info())
