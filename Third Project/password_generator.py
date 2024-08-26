import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    if password:
        print("Generated Password is : ", password)

if __name__ == "__main__":
    main()
