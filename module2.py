import PIL

# Import Libraries
from PIL import Image

image = Image.open("readonlytext.png")
#image.show()

import Image
import pytesseract
#dir(pytesseract)
#help(pytesseract.image_to_string)

import inspect
src = inspect.getsource(pytesseract.image_to_string)
print(src)

text = pytesseract.image_to_string(image)
print(text)
