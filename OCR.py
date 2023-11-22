from PIL import Image
from pytesseract import pytesseract

path_to_tesseracct = r"D:\Pytesseract\tesseract.exe"
image_path = r"Money\result1.png"

img = Image.open(image_path)

pytesseract.tesseract_cmd = path_to_tesseracct

# Pass the image through pytesseract
text = pytesseract.image_to_string(img)

print(text)
