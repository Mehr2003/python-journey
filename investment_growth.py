capital = int(input("capital:"))
rate = float(input("growth rate:"))
month = int(input("months:"))

if rate>1:
    rate =  rate / 100


for x in range (1, month+1):
    capital = capital + (rate*capital)
    print("Month", x, "=", capital)