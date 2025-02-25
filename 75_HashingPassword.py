# Hashing Password
import hashlib

def hash_password():
    # Take user input for the password
    password = input("Enter your password: ")
    
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Print the hashed password
    print(f"Hashed Password (SHA-256): {hashed_password}")

# Run the function
hash_password()
