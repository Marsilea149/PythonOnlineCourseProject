'''
#Import the pilow library
import PIL

#Find out PIL version
print(PIL.VERSION)
#Find out pillow version
print(PIL.PILLOW_VERSION)
#help about the content of PIL
#help(PIL)
#details about PIL
print(dir(PIL))

from PIL import Image 
#help(Image)

#help(Image.open)

file="/home/bingbing/Documents/PythonCourse/marsielaCartoon.jpeg"
image=Image.open(file)
#print(image)

import inspect
print("The type of the image is " + str(type(image)))
print(inspect.getmro(type(image)))
#Show the image in a window
#image.show()

# copy an image
#help(image.copy)

#save an image
#help(image.save)

#save a image in a new format
image.save("marsileaCartoonCopy.gif")
#image=Image.open("marsileaCartoonCopy.gif")
print("The new image has as type: \n" + str(inspect.getmro(type(image))))

#filter objects
from PIL import ImageFilter

#help(ImageFilter)


#convert image into RGB mode
image=image.convert('RGB')

blurred_image=image.filter(PIL.ImageFilter.BLUR)
blurred_image.show()

contour_image=image.filter(PIL.ImageFilter.CONTOUR)
contour_image.show()

detail_image=image.filter(PIL.ImageFilter.DETAIL)
detail_image.show()

ee_image=image.filter(PIL.ImageFilter.EDGE_ENHANCE)
ee_image.show()

eem_image=image.filter(PIL.ImageFilter.EDGE_ENHANCE_MORE)
eem_image.show()

emboss_image=image.filter(PIL.ImageFilter.EMBOSS)
emboss_image.show()

fe_image=image.filter(PIL.ImageFilter.FIND_EDGES)
fe_image.show()

sharpen_image=image.filter(PIL.ImageFilter.SHARPEN)
sharpen_image.show()

sm_image=image.filter(PIL.ImageFilter.SMOOTH)
sm_image.show()

smm_image=image.filter(PIL.ImageFilter.SMOOTH_MORE)
smm_image.show()

#Print the size of an image
print("{}x{}".format(image.width, image.height))

#help(image.crop)

#Crop an image
cropped_image = image.crop((50,0,100,200))
cropped_image.show()

#Draw a bounding box on an image
from PIL import ImageDraw
drawing_object = ImageDraw.Draw(image)
drawing_object.rectangle((50,50,100,150),fill = None, outline = 'red')
image.show()
'''

# CREAT A CONTACT SHEET 

#IMPORT ALL LIBRARY FUNCTIONS
import PIL
from PIL import Image
from PIL import ImageEnhance 
from PIL import ImageColor

# LOAD THE IMAGE 
file = "umich.jpeg"
image = Image.open(file)
image.save("umich.gif")
image = image.convert('RGB')
# DISPLAY THE IMAGE
#image.show()
'''
# GENERATE 10 IMAGES OF DIFFERENT BRIGHTNESS
enhancer = ImageEnhance.Brightness(image)
images = []
for i in range(0,10):
	images.append(enhancer.enhance(i/10))
	#images[i].show()
print(images)

# COMPOSITE THESE 10 IMAGES ONE ABOVE THE OTHER IN A CONTACT SHEET
first_image = images[0]
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width, 10*first_image.height))
current_location = 0
for img in images:
	#past the current image into the contact sheet
	contact_sheet.paste(img, (0, current_location))
	#update the current location counter
	current_location = current_location + image.height
#resize the contact sheet
contact_sheet = contact_sheet.resize((first_image.width,first_image.height*4))
contact_sheet.show()

# COMPOSIT THE IMAGES INTO A 3 BY 3 GRID
first_image = images[0]
contact_sheet = PIL.Image.new(first_image.mode, (3*first_image.width, 3*first_image.height))
x = 0
y = 0
for img in images[1:]:
	#paste the current image into the contact sheet
	contact_sheet.paste(img,(x,y),"yellow")
	#update the x position
	if x+first_image.width == contact_sheet.width: 
		x = 0
		y = y + first_image.height
	else:
		x = x + first_image.width
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2), int(contact_sheet.height/2)))
contact_sheet.show()

'''
images = []
for i in range(0,10):
	images.append(image)

# COMPOSIT THE IMAGES INTO A 3 BY 3 GRID
first_image = images[0]
contact_sheet = PIL.Image.new(first_image.mode, (3*first_image.width, 3*first_image.height))
x = 0
y = 0
row = 0
col = 0
for img in images[1:]:
	
	#create a Pixel Map
	pixels = img.load()
	
	#TRANSFORM COLOR OF EACH PIXEL
	for i in range(img.width):
		for j in range(img.height):
			#Get Pixel
			pixel = img.getpixel((i,j))
		
			#Get R, G, B values (which are int from 0 to 255)
			red = pixel[0]
			green  = pixel[1]
			blue = pixel[2]
		
			if row == 0:
				red = red
				green = green
				blue = 255
			elif row == 1:
				red = 255
				green = green
				blue = blue
			else: 
				red = red
				green = 255
				blue = blue
			
			if col == 0:
				intensity = 0.1
			elif col == 1:
				intensity = 0.5
			else: 
				intensity = 0.9
		
			#Color transformation
			pixels[i,j] = (int(red*intensity), int(green*intensity), int(blue*intensity))
	
	#paste the current image into the contact sheet
	contact_sheet.paste(img,(x,y))
	
	#update the x position
	if x+first_image.width == contact_sheet.width: 
		x = 0
		y = y + first_image.height
		col = col + 1
	else:
		x = x + first_image.width
		row = row + 1
		
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2), int(contact_sheet.height/2)))
contact_sheet.show()



