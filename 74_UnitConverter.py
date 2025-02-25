# Unit Converter
def convert_length():
    print("\nLength Converter:")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Centimeters to Meters")
    print("4. Meters to Centimeters")
    
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        meters = float(input("Enter length in meters: "))
        print(f"{meters} meters = {meters / 1000} kilometers")
    elif choice == 2:
        kilometers = float(input("Enter length in kilometers: "))
        print(f"{kilometers} kilometers = {kilometers * 1000} meters")
    elif choice == 3:
        centimeters = float(input("Enter length in centimeters: "))
        print(f"{centimeters} centimeters = {centimeters / 100} meters")
    elif choice == 4:
        meters = float(input("Enter length in meters: "))
        print(f"{meters} meters = {meters * 100} centimeters")
    else:
        print("Invalid choice.")

def convert_weight():
    print("\nWeight Converter:")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    print("3. Pounds to Kilograms")
    print("4. Kilograms to Pounds")
    
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        kg = float(input("Enter weight in kilograms: "))
        print(f"{kg} kilograms = {kg * 1000} grams")
    elif choice == 2:
        grams = float(input("Enter weight in grams: "))
        print(f"{grams} grams = {grams / 1000} kilograms")
    elif choice == 3:
        pounds = float(input("Enter weight in pounds: "))
        print(f"{pounds} pounds = {pounds * 0.453592} kilograms")
    elif choice == 4:
        kg = float(input("Enter weight in kilograms: "))
        print(f"{kg} kilograms = {kg * 2.20462} pounds")
    else:
        print("Invalid choice.")

def convert_temperature():
    print("\nTemperature Converter:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius} Celsius = {celsius * 9/5 + 32} Fahrenheit")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit} Fahrenheit = {(fahrenheit - 32) * 5/9} Celsius")
    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius} Celsius = {celsius + 273.15} Kelvin")
    elif choice == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} Kelvin = {kelvin - 273.15} Celsius")
    else:
        print("Invalid choice.")

def unit_converter():
    print("Welcome to the Unit Converter!")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")
    
    choice = int(input("Choose a conversion category: "))
    
    if choice == 1:
        convert_length()
    elif choice == 2:
        convert_weight()
    elif choice == 3:
        convert_temperature()
    else:
        print("Invalid choice. Please try again.")

# Run the unit converter
unit_converter()
