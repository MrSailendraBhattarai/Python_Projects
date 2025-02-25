#Count Down Timer
import time

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(i)  # Prints each second on a new line
        time.sleep(1)

    print("Time's up! ⏰")

# Taking user input
try:
    total_time = int(input("Enter time in seconds: "))
    countdown_timer(total_time)
except ValueError:
    print("Please enter a valid number!")
