def main():
    print("Which function do you wish to run?\n1) write_name\n2) read_name\n3) numbers\n")
    choice = int(input("Enter the function number: "))
    if choice == 1:
        write_name()
    elif choice == 2:
        read_name()
    elif choice == 3:
        numbers()


def write_name():
    name_file = open("name.txt", "w")
    name = input("Enter your name: ")
    print(name, file=name_file)
    name_file.close()


def read_name():
    name_file = open("name.txt", "r")
    print("Your name is", name_file.read())
    name_file.close()


def numbers():
    name_file = open("numbers.txt", "r")
    total = 0
    for line in name_file:
        number = int(line)
        total = total + number
    print("Your total number is:", total)
    name_file.close()


main()
