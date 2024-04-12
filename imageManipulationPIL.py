"""
This script demonstrates various image manipulation techniques using the PIL library and numpy arrays.

Functions:
- copy_images: Downloads images from a list of URLs and saves them locally.
- flip_images: Flips images vertically and horizontally using numpy arrays and PIL functions.
- crop_images: Crops images using numpy arrays and PIL functions.
- change_pixels: Modifies specific pixels in an image using numpy arrays.
- overlay_images: Overlays one image on top of another using numpy arrays and PIL functions.
"""

import os
import requests
import matplotlib.pyplot as plt
from PIL import Image, ImageOps, ImageFont, ImageDraw
import numpy as np

# Rest of the code...
import requests
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


urls = [
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CV0101EN-SkillsNetwork/images%20/images_part_1/cat.png",
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CV0101EN-SkillsNetwork/images%20/images_part_1/lenna.png",
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-CV0101EN-SkillsNetwork/images%20/images_part_1/baboon.png"
]

for url in urls:
    response = requests.get(url, timeout=5)
    filename = os.path.basename(url)
    with open(filename, 'wb') as f:
        f.write(response.content)



#copying images
print("Copying images")
baboon = np.array(Image.open('baboon.png'))
plt.figure(figsize=(5,5))
plt.imshow(baboon)
plt.show()

#if we don't use copy - we will reference the original image memory location
A = baboon
#check if A and baboon are the same
print("are A and babboon the same? ", id(A) == id(baboon))

#However, if we apply method copy(), their memory addresses are different.
B = baboon.copy()
print("are B and babboon the same?", id(B) == id(baboon))
#There may be unexpected behaviours when two variables point to the same object in memory. Consider the array baboon. If we set all its entries to zero, all entires in A will become zero as well. However, as baboon and B points to different objects, the values in B will not be affected.
baboon[:, :, :] = 0
#compare baboon and A
plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(baboon)
plt.title("baboon")
plt.subplot(122)
plt.imshow(A)
plt.title("array A")
plt.show()
#compare baboon and b
plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(baboon)
plt.title("baboon")
plt.subplot(122)
plt.imshow(B)
plt.title("array B")
plt.show()

#We can compare the variables baboon and array A:
plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(baboon)
plt.title("baboon")
plt.subplot(122)
plt.imshow(A)
plt.title("array A")
plt.show()

#If a PIL function does not return a new image, the same principle applies.

#flipping images
print("Flipping images")
image = Image.open("cat.png")
plt.figure(figsize=(10,10))
plt.imshow(image)
plt.show()

array = np.array(image)
width, height, C = array.shape
print('width, height, C', width, height, C)

#cast it to an array and find its shape
array = np.array(image)
width, height, C = array.shape
print('width, height, C', width, height, C)

#to flip   create an array of same size with datatype np.unit8
array_flip = np.zeros((width, height, C), dtype=np.uint8)

#y_flip = np.zeros((width, height, C), dtype=np.uint8)
#We assign the first row of pixels of the original array to the new array’s last row. We #repeat the process for every row, incrementing the row number from the original array #and decreasing the new array’s row index to assign the pixels accordingly. After #excecuting the for loop below, array_flip will become the flipped image.

for i, row in enumerate(array):
    array_flip[width - 1 - i, :, :] = row

print("the flip() method of ImageOps flips images vertically.")
im_flip = ImageOps.flip(image)
plt.figure(figsize=(5,5))
plt.imshow(im_flip)
plt.show()

print("the mirror() method of ImageOps flips images horizontally.")
im_mirror = ImageOps.mirror(image)
plt.figure(figsize=(5,5))
plt.imshow(im_mirror)
plt.show()

print("the transpose() method of ImageOps flips images horizontally.")
im_flip = image.transpose(1)
plt.imshow(im_flip)

flip = {
    "FLIP_LEFT_RIGHT": Image.FLIP_LEFT_RIGHT,
    "FLIP_TOP_BOTTOM": Image.FLIP_TOP_BOTTOM,
    "ROTATE_90": Image.ROTATE_90,
    "ROTATE_180": Image.ROTATE_180,
    "ROTATE_270": Image.ROTATE_270,
    "TRANSPOSE": Image.TRANSPOSE,
    "TRANSVERSE": Image.TRANSVERSE
}

print(flip)

#We can plot each of the outputs using the different parameter values:
for key, values in flip.items():
    plt.figure(figsize=(10,10))
    plt.subplot(1,2,1)
    plt.imshow(image)
    plt.title("orignal")
    plt.subplot(1,2,2)
    plt.imshow(image.transpose(values))
    plt.title(key)
    plt.show()


#CROPPING AN IMAGE
print("Cropping images")
upper = 150
lower = 400
crop_top = array[upper: lower, :, :]
plt.figure(figsize=(5,5))
plt.imshow(crop_top)
plt.show()

#Consider the array crop_top: we can also crop horizontally. The variable right is the index of the first column that we would like to include in the image and the variable left is the index of the last column we would like to include in the image.

left = 150
right = 400
crop_horizontal = crop_top[:, left:right, :]
plt.figure(figsize=(5,5))
plt.imshow(crop_horizontal)
plt.show()

#You can crop the PIL image using the crop() method, using the parameters from above Set the cropping area with box=(left, upper, right, lower).

image = Image.open("cat.png")
crop_image = image.crop((left, upper, right, lower))
plt.figure(figsize=(5,5))
plt.imshow(crop_image)
plt.show()

#also flip the new image
crop_image = crop_image.transpose(Image.FLIP_LEFT_RIGHT)
plt.figure(figsize=(5,5))
plt.imshow(crop_image)
plt.show()


#changing specific pixels
print("Changing specific pixels")
array_sq = np.copy(array)
array_sq[upper:lower, left:right, 1:2] = 0

plt.figure(figsize=(5,5))
plt.subplot(1,2,1)
plt.imshow(array)
plt.title("orignal")
plt.subplot(1,2,2)
plt.imshow(array_sq)
plt.title("Altered Image")
plt.show()

#we can also use imageDraw to draw on the image
#copy image
image_draw = image.copy()
#The draw constructor creates an object that can be used to draw in the given image. The input im is the image we would like to draw in.
image_fn = ImageDraw.Draw(im=image_draw)

#Whatever method we apply to the object image_fn, will change the image object image_draw.

#We can draw a rectangle using the rectangle function, two important parameters include: xy – the coordinates bounding box and fill – Color of the rectangle.

shape = [left, upper, right, lower]
image_fn.rectangle(xy=shape, fill="red")

#plot the image
plt.figure(figsize=(10,10))
plt.imshow(image_draw)
plt.show()

#get fonts from PIL library and draw text on the image
image_fn.text(xy=(0,0), text="box", fill=(0,0,0))

plt.figure(figsize=(10,10))
plt.imshow(image_draw)
plt.show()

#overlaying images one on the other
image_lenna = Image.open("lenna.png")
array_lenna = np.array(image_lenna)

#We can reassign the pixel values as follows:
array_lenna[upper:lower, left:right, :] = array[upper:lower, left:right, :]
plt.imshow(array_lenna)
plt.show()

#paste the image
image_lenna.paste(crop_image, box=(left, upper))
#We can see the method copy() applies to some PIL objects. We create two image objects, we set new_image to the image, and we use the method copy() for the copy_image object.
plt.imshow(image_lenna)
plt.show()

image = Image.open("cat.png")
new_image = image
copy_image = image.copy()

#we see that the same memory address relationship exists. For example, if we don't use the method copy(), the image object has the same memory address as the original PIL image object.
id(image) == id(new_image)
#If we change the object image, new_image will change, but copy_image will remain the same:
image_fn = ImageDraw.Draw(im=image)
image_fn.text(xy=(0,0), text="box", fill=(0,0,0))
image_fn.rectangle(xy=shape, fill="red")

# write your script here

from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np

# Open the image
im = Image.open('baboon.png')

# Flip and mirror the image
im_flip = ImageOps.flip(im)
im_mirror = ImageOps.mirror(im)

# Convert the images back to numpy arrays for displaying with matplotlib
im_flip_np = np.array(im_flip)
im_mirror_np = np.array(im_mirror)

# Create a new figure
plt.figure(figsize=(10,10))

# Display the flipped image
plt.subplot(121)
plt.imshow(im_flip_np)

# Display the mirrored image
plt.subplot(122)
plt.imshow(im_mirror_np)

# Show the plot
plt.show()
