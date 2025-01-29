
# pip install pillow
# Image Mirroring

from pillow import Image

Original=input('Enter Image Name : ')

# Image.open(Original)

img=Image.open(Original)

Mirror=img.transpose(Image.FLIP_LEFT_RIGHT)
Mirrored='Mirror.png'

Mirror.save(Mirrored)

Image.open(Mirrored)