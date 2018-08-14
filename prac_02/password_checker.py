min_length = 5
max_length = 15
special_chars_required = True
special_characters = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", min_length, "and", max_length,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if special_chars_required:
        print("\tand 1 or more special characters: ", special_characters)
    password = input("Enter your password: ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("Enter your password: ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    if len(password) < 5 or len(password) > 15:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isupper():
            count_upper = count_upper + 1
        elif char.islower():
            count_lower = count_lower + 1
        elif char.isnumeric():
            count_digit = count_digit + 1
        elif char in special_characters:
            count_special = count_special + 1
        print(count_special)

    if count_lower == 0 or count_upper == 0 or count_digit == 0 or count_special == 0:
        return False
    else:
        return True


main()
