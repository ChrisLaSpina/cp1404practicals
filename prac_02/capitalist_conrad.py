"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

OUTPUT_FILE = "OUTPUT_FILE.txt"
max_increase = 0.175  # 17.5%
max_decrease = 0.05  # 5%
min_price = 1.0
max_price = 100.0
initial_price = 10.0
days = 0

out_file = open(OUTPUT_FILE, 'w')
price = initial_price
print("${:,.2f}".format(price))

while min_price <= price <= max_price:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, max_increase)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-max_decrease, 0)

    price *= (1 + price_change)
    days = days + 1
    print("On day {0} price is ${1:,.2f}".format(days, price), file=out_file)

out_file.close()
