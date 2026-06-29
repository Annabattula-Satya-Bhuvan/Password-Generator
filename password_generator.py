import string
import secrets

# Characters to use
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

# Get password length from the user
length = int(input("Enter password length: "))

# Generate password
password = ""

for i in range(length):
    password += secrets.choice(all_characters)

print("\nGenerated Password:")
print(password)
