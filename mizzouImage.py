from PIL import Image # to work with imagery
import numpy as np # lib for operations on arrays
import math # for math operations
from IPython.display import display # for displaying our images

# open our image (because everyone loves cats)
rgb = Image.open('./mizzou.JPG') # the ./ refers to our local directory
# what size is it?
hsv_im = rgb.convert("HSV")
rgb_arr = np.array(rgb)
red = rgb_arr[:,:,0]
green = rgb_arr[:,:,1]
blue = rgb_arr[:,:,2]

hsv = np.array(hsv_im)

hue = hsv[:,:,0]
sat = hsv[:,:,1]
val = hsv[:,:,2]
xsize, ysize = hue.shape # get the dimensionality
lo,hi = 40, 220
lo = int((lo * 255) / 360)
hi = int((hi * 255) / 360)

for i in range(xsize):
    for j in range(ysize):
        if( sat[i,j] > 20):
            if( hue[i,j] >= lo and hue[i,j] <= hi ):
                val[i, j] = 0

            
        
          
hsv_image = Image.merge("HSV", (Image.fromarray(hue), Image.fromarray(sat), Image.fromarray(val)))
hsv_array = np.array(hsv_image)
hue2 = hsv_array[:,:,0]
display(Image.fromarray( hue2 ).resize((math.floor(xsize/2),math.floor(ysize/2)),Image.BICUBIC))
hue_image = Image.fromarray(hue2)
#hue_image.show()
#sat_image = Image.fromarray(sat)
val_image = Image.fromarray(val)
#sat_image.show()
val_image.show()
rbg_final = hsv_image.convert("RGB")
rbg_final.show()

