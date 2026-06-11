students={
    "stu1": {
        "name": "Mehr",
        "economics": 18,
        "math": 15,
        "english": 20
    },
    "stu2": {
        "name": "Amir",
        "economics": 15,
        "math": 16,
        "english": 13
    },
    "stu3": {
        "name": "Mobina",
        "economics": 19,
        "math": 13,
        "english": 20
    }
}

#print(students)

for key, student in students.items():
    average = (student["economics"] + student["math"] + student["english"]) / 3
    student["average"] = average


highest_student = students["stu1"]["name"]
highest_average = -1

for key, student in students.items():
    if student["average"] > highest_average:
        highest_average = student["average"]
        highest_student = student["name"]

print(highest_student)