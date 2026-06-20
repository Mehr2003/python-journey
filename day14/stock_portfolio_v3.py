stocks = (
    ("AAPL", 210),
    ("TSLA", 310),
    ("MSFT", 180),
    ("NVDA", 450),
    ("GOOGL", 230)
)

def find_highest_stock(stocks):
    most_expensive_symbol = None
    highest_price = -1
    for symbol, price in stocks:
        if price > highest_price:
            highest_price = price
            most_expensive_symbol = symbol
    return most_expensive_symbol, highest_price

def find_lowest_stock(stocks):
    cheapest_symbol = None
    lowest_price = 9999
    for symbol, price in stocks:
        if price < lowest_price:
            lowest_price = price
            cheapest_symbol = symbol
    return cheapest_symbol, lowest_price

def calculate_average_price(stocks):
    total = 0
    for symbol, price in stocks:
        total = total + price
        average = total / len(stocks)
    return average

def main():
    highest = find_highest_stock(stocks)
    lowest = find_lowest_stock(stocks)
    average = calculate_average_price(stocks)
    print(highest)
    print(lowest)
    print(average)
main()