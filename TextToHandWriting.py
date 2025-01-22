
# pip install pywhatkit
import pywhatkit as pw

txt=input("Enter Text to Convert to HandWriting : ")

pw.text_to_handwriting(txt,"text.png",[0,0,128])

print("End")