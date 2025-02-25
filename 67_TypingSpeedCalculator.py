# Typing Speed
import time

def typing_speed_test():
    print("Welcome to the Typing Speed Test! 🚀")
    sample_text = "The quick brown fox jumps over the lazy dog."
    print("\nType the following sentence as fast as you can:")
    print(f"📝 {sample_text}\n")

    input("Press ENTER when you are ready to start...\n")
    
    start_time = time.time()  # Start time
    user_input = input("Start typing: ")
    end_time = time.time()  # End time
    
    elapsed_time = end_time - start_time  # Time taken
    words = len(sample_text.split())  # Count words in the sample text

    if user_input.strip() == sample_text:
        wpm = (words / elapsed_time) * 60  # Words per minute formula
        print(f"\n✅ Perfect! Your typing speed is {wpm:.2f} WPM ⌨️")
    else:
        print("\n⚠ Text does not match exactly. Try again for accuracy!")

    print(f"⏳ Time taken: {elapsed_time:.2f} seconds.")

# Run the typing test
typing_speed_test()