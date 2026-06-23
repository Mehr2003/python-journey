class Crypto:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    def is_expensive(self):
        if self.price > 1000:
            return True
        else:
            return False
    def show_info(self):
        status = "Expensive!" if self.is_expensive() else "Not Expensive!"
        return f"{self.name} | {self.price} | {status}"
    
cryptos = [
    Crypto("BTC", 66100),
    Crypto("ETH", 1760),
    Crypto("BNB", 650),
    Crypto("SOL", 92),
    Crypto("XRP", 1.4),
    Crypto("ADA", 0.28),
    Crypto("DOGE", 0.10),
    Crypto("TRX", 0.31)
]

def find_most_expensive(cryptos):
    most_expensive_crypto = None
    highest_price = -1
    for crypto in cryptos:
        if crypto.price > highest_price:
            highest_price = crypto.price
            most_expensive_crypto = crypto.name
    return most_expensive_crypto, highest_price
result = find_most_expensive(cryptos)
print("most expensive crypto:", result)

def find_cheapest(cryptos):
    cheapest_crypto = None
    lowest_price = 9999
    for crypto in cryptos:
        if crypto.price < lowest_price:
            lowest_price = crypto.price
            cheapest_crypto = crypto.name
    return cheapest_crypto, lowest_price
result = find_cheapest(cryptos)
print("cheapest crypto:", result)

def better_cryptos(cryptos):
    count = 0
    for crypto in cryptos:
        if crypto.price > 1000:
            count += 1 
    return count
result = better_cryptos(cryptos)
print("number of better cryptos:", result)

print("information:")
for crypto in cryptos:
    print(crypto.show_info())