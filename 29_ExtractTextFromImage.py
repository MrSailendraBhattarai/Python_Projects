
# pip install pytesseract
# Extract Text fro Image


from PIL import Image 
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_image():
    try:
        
        img_path = input("Enter the path to the image: ")
        img = Image.open(img_path)  # Open the image

        
        extracted_text = pytesseract.image_to_string(img)

        print("\nExtracted Text:")
        print(extracted_text)

    except FileNotFoundError:
        print("Error: Image file not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

extract_text_from_image()



