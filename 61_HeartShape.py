
# Red Heart
import numpy as np
import matplotlib.pyplot as plt

# Parametric equations for a heart shape
t = np.linspace(0, 2 * np.pi, 1000)

# Heart shape equations
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Plot the heart shape
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red')  # Red heart
plt.fill(x, y, color='red')  # Fill the heart with red color

# Set aspect ratio to equal to ensure the heart is not distorted
plt.gca().set_aspect('equal', adjustable='box')

# Remove axes for a cleaner look
plt.axis('off')

# Show the plot
plt.title("Red Heart")
plt.show()
