#Emi Calculator
def calculate_emi(principal, rate_of_interest, tenure):
    # Convert annual interest rate to monthly and percentage to decimal
    monthly_rate = rate_of_interest / (12 * 100)
    
    # Convert tenure from years to months
    tenure_months = tenure * 12
    
    # EMI formula: EMI = [P * r * (1+r)^n] / [(1+r)^n - 1]
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
    
    return emi

def emi_calculator():
    print("Welcome to the EMI Calculator! 🚀")
    
    try:
        # Taking user inputs for loan amount, interest rate, and loan tenure
        principal = float(input("Enter the loan amount (Principal): "))
        rate_of_interest = float(input("Enter the annual interest rate (in %): "))
        tenure = int(input("Enter the loan duration (in years): "))
        
        # Calculating EMI
        emi = calculate_emi(principal, rate_of_interest, tenure)
        
        print(f"\nYour EMI is: Rs {emi:.2f} per Months")
        
        total_payment = emi * tenure * 12
        total_interest = total_payment - principal
        
        print(f"Total amount to be paid over {tenure} years: Rs {total_payment:.2f}")
        print(f"Total interest payable: Rs {total_interest:.2f}")
    
    except ValueError:
        print("⚠️ Invalid input! Please enter numerical values.")

# Run the EMI calculator
emi_calculator()
