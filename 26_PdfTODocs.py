
# pip install pdf2docx

from pdf2docx import Converter

pdf=input('Enter Pdf Name : ') # give your pdf name
docx=input('Enter Docx Name to Save : ')
cv=Converter(pdf)
cv.convert(docx)

cv.close()
