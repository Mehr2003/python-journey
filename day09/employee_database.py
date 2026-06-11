employees = {
    "emp1" : {
        "name":"Ali", 
        "salary": 200,
        "department": "social"
    }, 
    "emp2" :{
        "name":"Mobin", 
        "salary":1000, 
        "department":"manager"
    }, 
    "emp3" :{
        "name":"Reza",
        "salary": 750,
        "department": "writer"
    },
    "emp4" :{
        "name":"Mahdi",
        "salary":1540,
        "department":"reader"
    }
}

for x, obj in employees.items():
    print("name:", obj["name"])
for y, obj in employees.items():
    print("salary:", obj["salary"])