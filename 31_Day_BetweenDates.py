
from datetime import datetime

first_date = input('Enter First Date (d/m/y) : ')
second_date = input('Enter Second Date (d/m/y) : ')

first_date_obj = datetime.strptime(first_date, '%d/%m/%Y')
second_date_obj = datetime.strptime(second_date, '%d/%m/%Y')

diff = abs(first_date_obj - second_date_obj)

print(f"Days between {first_date} & {second_date} is: {diff.days}")
