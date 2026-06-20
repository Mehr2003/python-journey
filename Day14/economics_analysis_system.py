economies = (
    ("USA", 4.2, 3.8, 5.1),
    ("Germany", 2.5, 4.0, 4.8),
    ("Japan", 1.8, 2.9, 3.7),
    ("China", 5.4, 5.1, 5.7)
)

def country_average_growth(g22, g23, g24):
    average = (g22 + g23 + g24)/3
    return average

def find_best_country(economies):
    best_country = None
    highest_growth = -1
    for name, g22, g23, g24 in economies:
        average = country_average_growth(g22, g23, g24)
        if average > highest_growth:
            highest_growth = average
            best_country = name
    return best_country, highest_growth
result = find_best_country(economies)
#print("best country:")
#print("name:", result[0])
#print("average:", result[1])

def find_worst_country(economies):
    worst_country = None
    lowest_growth = 9999
    for name, g22, g23, g24 in economies:
        average = country_average_growth(g22, g23, g24)
        if average < lowest_growth:
            lowest_growth = average
            worst_country = name
    return worst_country, lowest_growth
result = find_worst_country(economies)
#print("worst country:")
#print("name:", result[0])
#print("average:", result[1])

def country_report(economies):
    for name, g22, g23, g24 in economies:
        average = country_average_growth(g22, g23, g24)
        print(name, ":", average)

def main():
    best = find_best_country(economies)
    worst = find_worst_country(economies)
    country_report(economies)
    print("best:", best)
    print("worst:", worst)
main()
        

        
