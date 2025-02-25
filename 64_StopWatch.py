# Stop Watch
import time

def stopwatch():
    print("Press ENTER to start the stopwatch.")
    print("Press CTRL + C to stop the stopwatch.")
    
    input()  # Wait for user to press Enter
    print("Stopwatch started...")

    start_time = time.time()  # Record the start time
    
    try:
        while True:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(int(elapsed_time), 60)
            print(f"Elapsed Time: {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)  # Update every second
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")
        mins, secs = divmod(int(time.time() - start_time), 60)
        print(f"Total Time: {mins:02d}:{secs:02d}")

# Run the stopwatch
stopwatch()

