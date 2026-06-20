economies = {
    "USA": 4.2,
    "Germany": 2.5,
    "Japan": 1.8,
    "China": 5.4
}

def best_country(economies):
    best_country = None
    highest_growth = -1
    for country, growth in economies.items():
        if growth > highest_growth:
            highest_growth = growth
            best_country = country
    return best_country, highest_growth
result = best_country(economies)
print(result)

def worst_country(economies):
    worst_country = None
    lowest_growth = 9999
    for country, growth in economies.items():
        if growth < lowest_growth:
            lowest_growth = growth
            worst_country = country
    return worst_country, lowest_growth
result = worst_country(economies)
print(result)

def growth_average(economies):
    total = 0
    for growth in economies.values():
        total += growth
    average = total / len(economies)
    return average
result = growth_average(economies)
print(result)

def better_countries(economies):
    count = 0
    for country, growth in economies.items():
        if growth > 3:
            count += 1
    return count
result = better_countries(economies)
print(result)