def main():
    MIN_LENGTH = 5
    password = get_valid_password(MIN_LENGTH)
    print("Your password is", "*" * len(password))


def get_valid_password(MIN_LENGTH):
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print("Please enter a new password that meets the required length.")
        password = input("Password: ")
    return password


main()
