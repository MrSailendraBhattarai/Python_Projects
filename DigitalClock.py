from tkinter import *
from time import strftime

# Create the main window
clock = Tk()
clock.title("Digital Clock")

# Create a label to display the time
lbl = Label(clock, font="arial 160 bold", bg="black", fg="white")
lbl.pack(anchor="center", fill="both", expand="yes")

# Define the function to update time
def time():
    string = strftime(" %H:%M:%S %p")  # Format the time string
    lbl.config(text=string)  
    lbl.after(1000, time)  # Schedule the function to run after 1 second (1000 ms)

# Call the time function to start the clock
time()

# Run the Tkinter event loop
mainloop()
