def main():
    COLOURS_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Aquamarine": "#7fffd4", "Azure": "#f0ffff",
               "Beige": "#f5f5dc", "Bisque": "#ffe4c4", "Black": "#000000", "White": "#ffffff"}

    colour = input("Enter colour name: ")
    while colour != "":
        if colour in COLOURS_CODE:
            print(colour, "is", COLOURS_CODE[colour])
        else:
            print("Invalid colour")
        colour = input("Enter colour name: ")

main()