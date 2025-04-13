import random
import string
import argparse

# Define the argument parser
parser = argparse.ArgumentParser(description="Generate a secure random password.")
parser.add_argument("minlen", type=int, nargs="?", default=8, help="Minimum length of the password (default: 8).")
parser.add_argument("maxlen", type=int, nargs="?", default=12, help="Maximum length of the password (default: 12).")
parser.add_argument("--lowercase", action="store_true", help="Include lowercase letters.")
parser.add_argument("--uppercase", action="store_true", help="Include uppercase letters.")
parser.add_argument("--special", action="store_true", help="Include special characters.")
parser.add_argument("--numbers", action="store_true", help="Include numbers.")

args = parser.parse_args()

# Validate minlen and maxlen
if args.minlen > args.maxlen:
    raise ValueError("Minimum length cannot be greater than maximum length.")

# Character sets
lowercase_chars = string.ascii_lowercase
uppercase_chars = string.ascii_uppercase
special_chars = string.punctuation
number_chars = string.digits

# Build the pool of possible characters
possible_password_chars = []
if args.lowercase:
    possible_password_chars += lowercase_chars
if args.uppercase:
    possible_password_chars += uppercase_chars
if args.special:
    possible_password_chars += special_chars
if args.numbers:
    possible_password_chars += number_chars

# Ensure at least one character type is selected
if not possible_password_chars:
    raise ValueError("At least one character type must be selected (use --lowercase, --uppercase, --special, or --numbers).")

# Generate the password
password_length = random.randint(args.minlen, args.maxlen)
password = [
    random.choice(lowercase_chars) if args.lowercase else "",
    random.choice(uppercase_chars) if args.uppercase else "",
    random.choice(special_chars) if args.special else "",
    random.choice(number_chars) if args.numbers else "",
]

# Fill the rest of the password with random characters from the pool
password += random.choices(possible_password_chars, k=password_length - len(password))
random.shuffle(password)

# Print the final password
print("Generated Password:", ''.join(password))
