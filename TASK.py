import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Please enter a valid integer.")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get the desired password length from the user
length = get_password_length()

# Generate the password
password = generate_password(length)
print("Generated password:", password)