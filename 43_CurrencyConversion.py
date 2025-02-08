
# currency Converter
from currency_converter import CurrencyConverter

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyConverter()
    try:
        converted_amount = c.convert(amount, from_currency, to_currency)
        print(f"\n💱 Conversion Rate: {amount} {from_currency} = {converted_amount:.2f} {to_currency}\n")
    except ValueError:
        print("❌ Error: Invalid currency code or unsupported conversion.")

# Taking user input
amount = float(input("Enter amount: "))
from_currency = input("Enter from currency code (e.g., USD, EUR, INR): ").upper()
to_currency = input("Enter to currency code (e.g., USD, EUR, INR): ").upper()

convert_currency(amount, from_currency, to_currency)
