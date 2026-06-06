economics = int(input("your economics grade:"))
math = int(input("your math grade:"))
english = int(input("your english grade:"))

def admission_check (economics, math, english):
    if (economics>=15 and math>=15 and english>=15):
        print ("accepted!")
    else:
        print ("rejected!")
admission_check(economics, math, english )