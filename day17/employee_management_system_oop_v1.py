class Employee:
    def __init__(self, name, salary, age) -> None:
        self.name = name
        self.salary = salary
        self.age = age
    
    def get_salary(self):
        return self.salary
    
    def earner_is_higher(self):
        if self.salary > 1500:
            return True
        else:
            return False
    def apply_raise(self, percent):
        self.salary = self.salary + (self.salary * (percent / 100))
        return self.salary
    def show_info(self):
        return f"{self.name} | Salary: {self.salary} | Age: {self.age}"
    
Ali = Employee("Ali", 1200, 25)
Sara = Employee("Sara", 1800, 31)
Reza = Employee("Reza", 2200, 28)
Maryam = Employee("Maryam", 1600, 35)
Amir = Employee("Amir", 900, 22)
Niloofar = Employee("Niloofar", 2500, 29)
Parsa = Employee("Parsa", 1400, 26)
Yasaman = Employee("Yasaman", 1950, 27)
Arman = Employee("Arman", 1700, 30)
Sahar = Employee("Sahar", 2100, 24)


print(Ali.show_info())
print(Sara.show_info())
print(Reza.show_info())
print(Maryam.show_info())
print(Amir.show_info())
print(Niloofar.show_info())
print(Parsa.show_info())
print(Yasaman.show_info())
print(Arman.show_info())
print(Sahar.show_info())