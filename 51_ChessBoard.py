
# ChessBoard
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Create an 8x8 chessboard pattern
board = np.tile([1, 0], (8, 4))

# Shift every alternate row for proper chessboard pattern
for i in range(board.shape[0]):
    if i % 2 == 1:
        board[i] = np.roll(board[i], 1)

# Define black and white colors
cmap = ListedColormap(['black', 'white'])

# Display the chessboard
plt.matshow(board, cmap=cmap)
plt.xticks([])  # Remove x-axis ticks
plt.yticks([])  # Remove y-axis ticks
plt.show()
