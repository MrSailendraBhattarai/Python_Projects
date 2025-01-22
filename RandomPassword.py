
import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Define the character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure the password contains at least one of each type
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]
    
    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password to make it unpredictable
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
password_length = int(input("Enter the desired password length: "))
password = generate_password(password_length)
print(f"Generated Password: {password}")
