class Crypto:
    def __init__(self, name, price, amount) -> None:
        self.name = name
        self.price = price
        self.amount = amount
    def portfolio_value(self):
        portfolio_value = self.price*self.amount
        return portfolio_value
    def show_info(self):
        return f"{self.name} | {self.price} | {self.amount} | {self.portfolio_value()}" 
cryptos = [
    Crypto("BTC", 105000, 0.5),
    Crypto("ETH", 2600, 3),
    Crypto("BNB", 700, 8),
    Crypto("SOL", 150, 25),
    Crypto("XRP", 2.3, 1500),
    Crypto("ADA", 0.75, 4000),
    Crypto("DOGE", 0.18, 12000),
    Crypto("TRX", 0.32, 7000),
    Crypto("AVAX", 42, 60),
    Crypto("LINK", 18, 120)
]
def find_most_valuable_crypto(cryptos):
    most_valuable_crypto = None
    highest_value = -1
    for crypto in cryptos:
        if crypto.portfolio_value() > highest_value:
            highest_value = crypto.portfolio_value()
            most_valuable_crypto = crypto.name
    return most_valuable_crypto, highest_value
result = find_most_valuable_crypto(cryptos)
print(result)

def find_total_portfolio_value(cryptos):
    total = 0
    for crypto in cryptos:
        total += crypto.portfolio_value()
    return total
result = find_total_portfolio_value(cryptos)
print(result)

for crypto in cryptos:
    print(crypto.show_info())