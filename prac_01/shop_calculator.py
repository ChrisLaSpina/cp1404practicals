def main():
    total_cost = 0
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    for i in range(1, number_of_items + 1, 1):
        price = float(input("Price of item: "))
        total_cost = total_cost + price
    if total_cost > 100:
        discount = (total_cost * 10) / 100
        total_cost = total_cost - discount
    print("Total price for", number_of_items, "items is", total_cost)


main()
