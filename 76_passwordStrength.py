# Password Strength
import re

def check_password_strength(password):
    strength = {"Weak": 0, "Moderate": 1, "Strong": 2}
    
    if len(password) < 6:
        return "Weak"
    
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[@$!%*?&]", password))
    
    score = sum([has_lower, has_upper, has_digit, has_special])
    
    if score < 2:
        return "Weak"
    elif score == 2:
        return "Moderate"
    else:
        return "Strong"

if __name__ == "__main__":
    password = input("Enter a password: ")
    print(f"Password Strength: {check_password_strength(password)}")