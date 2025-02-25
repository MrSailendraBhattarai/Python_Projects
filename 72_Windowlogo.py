# Window Logo
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle for drawing
t = turtle.Turtle()
t.speed(3)

# Function to draw a square
def draw_square(color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()

# Drawing 4 squares (a 2x2 grid)
colors = ["#1a73e8", "#1a73e8", "#1a73e8", "#1a73e8"]
positions = [(-60, 60), (0, 60), (-60, 0), (0, 0)]

for i in range(4):
    draw_square(colors[i], positions[i][0], positions[i][1])

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
