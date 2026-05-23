import random
import string

print("=== Password Generator ===")

# User input
length = int(input("Enter password length: "))

# Characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Output
print("Generated Password:", password)