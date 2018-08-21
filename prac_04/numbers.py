def main():
    numbers = []
    for i in range(1, 6):
        number = float(input("Number: "))
        numbers.append(number)

    print("The first number is {0}".format(numbers[0]))
    print("The last number is {0}".format(numbers[4]))
    print("The smallest number is {0}".format(min(numbers)))
    print("The largest number is {0}".format(max(numbers)))
    print("The average of the numbers is {0}".format(sum(numbers) / len(numbers)))


main()
