number1 = int(input("your first grade:"))
number2 = int(input("your second grade:"))
number3 = int(input("your third grade:"))

grades = [number1, number2, number3]
print(grades)

Average=sum(grades)/len(grades)

print("your average=", Average)


