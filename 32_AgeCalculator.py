
# Age Calculator
from datetime import datetime

birth_date = input('Enter Birth Date (d/m/y) : ')

# Convert the input string to a datetime object
birth_date_obj = datetime.strptime(birth_date, '%d/%m/%Y')

# Calculate the current date
current_date_obj = datetime.now()

# Calculate the age in years
age = current_date_obj.year - birth_date_obj.year

# Adjust the age if the birthday hasn't occurred yet this year
if (current_date_obj.month, current_date_obj.day) < (birth_date_obj.month, birth_date_obj.day):
    age -= 1

# Output the age
print(f"Your age is: {age} years")
