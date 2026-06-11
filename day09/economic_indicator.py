countries = {
    "country1":{
        "name":"Iran",
        "inflation":52.6
    }, 
    "country2":{
        "name":"China",
        "inflation":3.4
    },
    "country3":{
        "name":"Sweden",
        "inflation":0.3
    }
}

for x, obj in countries.items():
    print(obj["name"], ":", obj["inflation"])
