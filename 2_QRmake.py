

#pip install qrcode[PIL]
# QR Code
import qrcode as qr

user_input=input("What do you want to make Qr : ")
name=input("Write File Name of QR : ")
img=qr.make(user_input)
img.save(f"{name}.png")