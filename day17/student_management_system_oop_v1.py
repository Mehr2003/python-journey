class student:
    def __init__(self, name, economics, math, english) -> None:
        pass
        self.name = name
        self.economics=economics
        self.math=math
        self.english=english
    def calculate_average(self):
        average = (self.economics + self.math + self.english)/3
        return average
    def pass_or_fail(self):
        average = self.calculate_average()
        if average >= 17:
            return True
        else:
            return False
    def show_info(self):
        status = "Pass!" if self.pass_or_fail() else "Fail!"
        return f"{self.name} -> Average:{self.calculate_average()} -> {status}"
    
Reza = student("Reza", 14, 18, 17.5)
Ali = student("Ali", 20, 12.75, 13)
Mehrsa = student("Mehrsa", 20, 18, 19.75)
Samane = student("Samane", 17, 16.5, 14.75)

print ("Reza")
print("Average:", Reza.calculate_average())
print(Reza.pass_or_fail())
print ("Ali")
print("Average:", Ali.calculate_average())
print(Ali.pass_or_fail())
print ("Mehrsa")
print("Average:", Mehrsa.calculate_average())
print(Mehrsa.pass_or_fail())
print ("Samane")
print("Average:", Samane.calculate_average())
print(Samane.pass_or_fail())

print(Reza.show_info())
print(Ali.show_info())
print(Mehrsa.show_info())
print(Samane.show_info())
