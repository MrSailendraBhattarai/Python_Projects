

# Email Validation using Regex

import re

condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email=input("Enter Your E-mail : ")

if re.search(condition,user_email):
    print("Right E-mail")
else:
    print("Wrong E-mail")