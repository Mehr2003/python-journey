students = (("Amin", 16, 13, 17), ("Mehr", 19, 20, 17), ("Sara", 13, 14, 16))

def stu_avg(economics, math, english):
    return (economics+math+english)/3

for name, economics, math, english in students:
    average = stu_avg(economics, math, english)
    print(name, ":", average)