#Import Python Imaging Library (PIL)
import PIL
#Check the version of the library
print("Used Pillow version: " + PIL.PILLOW_VERSION)

#help(PIL) #Help with the built-in documentation of PIL
dir(PIL) # 

from PIL import Image
#help(Image)

file = "umich.gif"
image = Image.open(file)
#image.show() #Display the image in the screen
print(image)  #Print image info

import inspect
print("The type of the image is " + str(type(image)))
inspect.getmro(type(image))

from PIL import ImageFilter
image = image.convert('RGB')

blurred_image = image.filter(PIL.ImageFilter.BLUR)
blurred_image.show()
print("{}x{}".format(image.width, image.height))

cropped_image = image.crop((50,0,190,150))
cropped_image.show()