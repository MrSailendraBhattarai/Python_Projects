

# Custom QR Code making

import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
box_size=10,border=4)

user_input=input("What do you want to make Qr : ")
color=input("Which color QR You Want : ")
bg=input("Which Color Background You Want : ")
name=input("Write File Name of QR : ")

qr.add_data(user_input)
qr.make(fit=True)
img=qr.make_image(fill_color=f'{color}',back_color=f'{bg}')

img.save(f"{name}.png")
