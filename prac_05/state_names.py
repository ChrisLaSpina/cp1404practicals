"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


def main():
    STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                   "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

    for part_name, full_name in STATE_NAMES.items():
        print(part_name, "is", full_name)

    state = input("Enter short state: ")
    while state != "":
        if state in STATE_NAMES:
            print(state, "is", STATE_NAMES[state])
        else:
            print("Invalid short state")
        state = input("Enter short state: ")


main()
