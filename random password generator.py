import string
import random
import secrets

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    selection_list = ''
    if use_letters:
        selection_list += string.ascii_letters
    if use_numbers:
        selection_list += string.digits
    if use_symbols:
        selection_list += string.punctuation

    if not selection_list:
        print("Please select at least one character type.")
        return None

    password = ''.join(secrets.choice(selection_list) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of your password: "))
    use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print("Generated Password:", password)
    else:
        print("Password generation failed. Please try again.")
main()