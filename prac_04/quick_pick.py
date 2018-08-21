import random


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for number in range(1, number_of_quick_picks + 1):
        for i in range(1, 7):
            print(random.randint(1, 45), end=" ")
        print()


main()
