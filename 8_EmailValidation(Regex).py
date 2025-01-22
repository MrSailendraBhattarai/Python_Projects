

# Email Validation using Regex

import re

# Enhanced regex pattern to validate email addresses
condition = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Prompt user for email input
user_email = input("Enter Your E-mail: ").strip()

# Validate email
if re.fullmatch(condition, user_email):
    print("Right E-mail")
else:
    print("Wrong E-mail")
