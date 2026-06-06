economics = int(input("economics grade:"))
statistics = int(input("statistics grade:"))
math = int(input("math grade:"))

average = (economics + statistics + math) / 3
print("average", average)

if average>17:
    print("excelent!")
elif 17>=average>=12:
    print("good")
else:
    print("need improvement!")
