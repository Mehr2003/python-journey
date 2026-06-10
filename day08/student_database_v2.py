stu1 = {
    "name":"mehr",
    "economics grade" : 20,
    "math grade" : 16,
    "english grade" : 17
}
#print (stu1)

av1 = (
    stu1["economics grade"] +
    stu1["math grade"] +
    stu1["english grade"]) / 3 
#print(av1)
           


stu2 = {
    "name":"amin",
    "economics grade" : 16,
    "math grade" : 18,
    "english grade" : 14
}
#print(stu2)

av2 = (
    stu2["economics grade"] +
    stu2["math grade"] +
    stu2["english grade"]) / 3 
#print(av2)

stu3 = {
    "name":"mahak",
    "economics grade" : 18,
    "math grade" : 13,
    "english grade" : 16
}
#print(stu3)

av3 = (
    stu3["economics grade"] +
    stu3["math grade"] +
    stu3["english grade"]) / 3 
#print(av3) 

#students = [stu1, stu2, stu3]


averages = [(stu1["name"], av1), (stu2["name"], av2), (stu3["name"], av3)]
#print(averages)

highest = stu1["name"], av1
for x in averages:
    if x>highest:
        highest = x
#print(highest)

print("best student=", highest[0])