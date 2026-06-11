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
    average = (student["economics"] + student["math"] + student["english"])/3
    print(student["name"],":", average)
