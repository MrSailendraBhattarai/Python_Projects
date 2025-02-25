
# Decimal to Binary Converter and Viceversa
def convert_number():
    while True:
        try:
            menu = int(input("\nChoose an option: \n 1. Decimal to Binary \n 2. Binary to Decimal \n 3. Exit\nOption: "))
            
            if menu == 1:
                dec = int(input("Input your decimal number:\nDecimal: "))
                print(f"Binary: {bin(dec)[2:]}")
            
            elif menu == 2:
                binary = input("Input your binary number:\nBinary: ")
                print(f"Decimal: {int(binary, 2)}")
            
            elif menu == 3:
                print("Exiting program. Goodbye! 👋")
                break  # Exit the loop
            
            else:
                print("⚠ Please choose a valid option (1, 2, or 3).")
        
        except ValueError:
            print("⚠ Invalid input! Please enter a valid number.")

# Run the program
convert_number()
