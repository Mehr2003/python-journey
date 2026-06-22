coins = {
    "BTC": 105000,
    "ETH": 2600,
    "SOL": 150,
    "BNB": 700,
    "ADA": 0.8
}
def find_most_expensive_coin(coins):
    most_expensive = None
    highest_price = -1
    for name, price in coins.items():
        if price > highest_price:
            highest_price = price
            most_expensive = name
    return most_expensive, highest_price
result = find_most_expensive_coin(coins)
print(result)

def find_cheapest_coin(coins):
    cheapest_coin = None
    lowest_price = 9999
    for name, price in coins.items():
        if price < lowest_price:
            lowest_price = price
            cheapest_coin = name
    return cheapest_coin, lowest_price
result = find_cheapest_coin(coins)
print(result)

def calculate_average(coins):
    total = 0 
    for price in coins.values():
        total += price
    average = total / len(coins)
    return average
result = calculate_average(coins)
print(result)

def count_upper_than1000(coins):
    count = 0
    for price in coins.values():
        if price > 1000:
            count += 1
    return count
result = count_upper_than1000(coins)
print(result)