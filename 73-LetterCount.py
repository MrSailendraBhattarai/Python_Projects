# Letter Count
from collections import Counter

def count_letters():
    # Get user input
    text = input("Enter a string to count letters: ")

    # Remove spaces and convert to lowercase for case-insensitive counting
    text = text.replace(" ", "").lower()

    # Count the frequency of each letter
    letter_count = Counter(text)

    # Display the results
    print("\nLetter Count:")
    for letter, count in letter_count.items():
        print(f"{letter}: {count}")

# Run the function
count_letters()
