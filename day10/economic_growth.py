old_gdp = float(input("your country's last year gdp="))
new_gdp = float(input("your country's gdp="))

def growth(old_gdp, new_gdp):
    return (new_gdp - old_gdp)/old_gdp*100
print("your growth=", growth(old_gdp, new_gdp), "%")