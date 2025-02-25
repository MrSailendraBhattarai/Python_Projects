# Otp generator
import random
import string

def generate_otp(length=6):
    # Generate a random OTP with digits (0-9)
    otp = ''.join(random.choices(string.digits, k=length))
    return otp

def otp_generator():
    print("Welcome to the OTP Generator! 🚀")
    
    # Generate OTP
    otp = generate_otp()
    
    print(f"Your OTP is: {otp}")
    
# Run the OTP generator
otp_generator()
