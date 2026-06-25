class Expense:
    def __init__(self, title, category, amount) -> None:
        self.title = title
        self.category = category
        self.amount = amount
    def show_info(self):
        return f"{self.title} | {self.category} | {self.amount}"
expenses = [
    Expense("Coffee", "Food", 5),
    Expense("Book", "Education", 20),
    Expense("Netflix", "Entertainment", 12),
    Expense("Gym", "Health", 30),
    Expense("Taxi", "Transport", 8),
    Expense("Lunch", "Food", 15),
    Expense("Course", "Education", 50),
    Expense("Movie", "Entertainment", 10),
    Expense("Medicine", "Health", 25),
    Expense("Bus", "Transport", 3)
]

def find_total_cost(expenses):
    total = 0
    for expense in expenses:
        total += expense.amount
    return total
result = find_total_cost(expenses)
print(result)

def find_highest_expense(expenses):
    expensive_title = None
    highest_expense = -1
    for expense in expenses:
        if expense.amount > highest_expense:
            highest_expense = expense.amount
            expensive_title = expense.title
    return expensive_title, highest_expense
result = find_highest_expense(expenses)
print(result)

def food_counting(expenses):
    count = 0
    for expense in expenses:
        if expense.category == "Food":
            count += 1
    return count
result = food_counting(expenses)
print(result)

def find_average_expense(expenses):
    total = find_total_cost(expenses)
    average = total / len(expenses)
    return average
result = find_average_expense(expenses)
print(result)

for expense in expenses:
    print(expense.show_info())