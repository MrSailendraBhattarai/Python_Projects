
# pip install pillow
# Image Mirroring

from PIL import Image

# Input image name
Original = input('Enter Image Name : ')

# Open the original image
img = Image.open(Original)

# Create a mirrored version by flipping horizontally (left to right)
Mirror = img.transpose(Image.FLIP_LEFT_RIGHT)

# Save the mirrored image
Mirrored = 'Mirrored_' + Original
Mirror.save(Mirrored)

# Open and display the mirrored image
Mirror.show()
