portfolio = {
    "AAPL": 210,
    "TSLA": 310,
    "MSFT": 180,
    "NVDA": 450,
    "GOOGL": 230
}
def calculate_average_price(portfolio):
    total = 0
    for price in portfolio.values():
        total += price
    average = total / len(portfolio)
    return average
#result = calculate_average_price(portfolio)
#print ("average:", result)

def find_most_expensive_stock (portfolio):
    best_portfolio = None
    highest_price  = -1
    for symbol, price in portfolio.items():
        if price > highest_price:
            highest_price = price
            best_portfolio = symbol
    return best_portfolio

def find_cheapest_stock (portfolio):
    worst_portfolio = None
    lowest_price = 9999
    for symbol, price in portfolio.items():
        if price < lowest_price:
            lowest_price = price
            worst_portfolio = symbol
    return worst_portfolio

def count_expensive_stocks (portfolio):
    count = 0
    for price in portfolio.values():
        if price > 250:
            count += 1
    return count
#result = count_expensive_stocks (portfolio)
#print("how many portfolios higher than 250?", result)

def portfolio_report(portfolio):
    for symbol, price in portfolio.items():
        print(f"{symbol} : {price}")

def main():
    average = calculate_average_price(portfolio)
    highest = find_most_expensive_stock (portfolio)
    lowest = find_cheapest_stock (portfolio)
    better = count_expensive_stocks (portfolio)
    portfolio_report(portfolio)
    print("average:", average)
    print("highest:", highest)
    print("lowest:", lowest)
    print("better than others:", better)
main()