def main():
    MIN_LENGTH = 5
    password = input("Password: ")
    if len(password) < MIN_LENGTH:
        print("Please enter a new password that meets the required length.")
        password = input("Password: ")
    else:
        print("Your password is", "*" * len(password))


main()
