from PIL import Image # to work with imagery
import numpy as np # lib for operations on arrays
import math # for math operations
from IPython.display import display # for displaying our images

# open our image (because everyone loves cats)
rgb = Image.open('./mizzou.JPG') # the ./ refers to our local directory
# what size is it?
xsize, ysize = rgb.size # get the dimensionality
green_img = np.array(rgb)
green_img[:,:,0] = 0
green_img[:,:,2] = 0
image = Image.fromarray(green_img)
# print is how we display statements to the user (text)
#print( "Image size is " + str(pil_im.size) ) 

# show it 
image.show()

rgb_im = Image.fromarray( rgb )
hsv_im = rgb_im.convert("HSV")
hsv = np.array( hsv_im )
hue = hsv[:,:,0]
sat = hsv[:,:,1]
val = hsv[:,:,2]