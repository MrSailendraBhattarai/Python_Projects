
# pip install fpdf
# Image to Pdf

from fpdf import FPDF as pdf

pdf.add_page()

img=input('Enter Image : ')
pdf.image(img,x=10,y=10,w=100)

pdf.set_font('Caliber',size=12)
pdf.ln(60)

pdf.cell(200,10,txt='Image to Pdf.',ln=True)

pdf.output('ImageToPdf.pdf')

print('Image_pdf.pdf')