import os
import string
import cv2
import requests
import numpy as np
import matplotlib.pyplot as plt

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

baboon = cv2.imread("baboon.png")
plt.figure(figsize=(3,5))
plt.imshow(cv2.cvtColor(baboon, cv2.COLOR_BGR2RGB))
plt.show()

A = baboon

id_A = id(A)
print(id_A)

B = baboon.copy()
id_B = id(B)
print(id_B)

baboon[:,:,] = 0

plt.figure(figsize=(5,5))
plt.subplot(121)
plt.imshow(cv2.cvtColor(baboon, cv2.COLOR_BGR2RGB))
plt.title("baboon")

plt.subplot(122)
plt.imshow(cv2.cvtColor(A, cv2.COLOR_BGR2RGB))
plt.title("array A")
plt.show()

plt.figure(figsize=(5,5))
plt.subplot(121)
plt.imshow(cv2.cvtColor(baboon, cv2.COLOR_BGR2RGB))
plt.title("baboon")
plt.subplot(122)
plt.imshow(cv2.cvtColor(B, cv2.COLOR_BGR2RGB))
plt.title("array B")
plt.show()
 

print('Flipping images')

image = cv2.imread("cat.png")
plt.figure(figsize=(5,5))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.show()
plt.close()

width, height, C = image.shape
import cv2 as cv

print('width, height, C', width, height, C)

array_flip = np.zeros((width, height, C), dtype=np.uint8)

for i, row in enumerate(image):
    array_flip[width-1-i, :, :] = row
    print("flipcode : ", i, "row: ")


     

for flipcode in [0, 1, -1]:
    im_flip =  cv2.flip(image, flipcode)
    print("flipcode : ", flipcode)
    plt.figure(figsize=(5,5))
    plt.imshow(cv2.cvtColor(im_flip, cv2.COLOR_BGR2RGB))
    plt.title("flipcode: "+str(flipcode))
    plt.show()
    cv2.imwrite('flipcode'+str(flipcode)+'.png', im_flip)
    print("flipcode : ", flipcode)
    plt.close()

print("Rotating images")
image = cv2.imread("cat.png")
plt.figure(figsize=(5,5))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.show()
plt.close()


im_flip = cv2.rotate(image, 0)
cv2.imwrite('rotate_zero.png', im_flip)

flip = {"ROTATE_90_CLOCKWISE": cv2.ROTATE_90_CLOCKWISE, "ROTATE_90_COUNTERCLOCKWISE": cv2.ROTATE_90_COUNTERCLOCKWISE, "ROTATE_180": cv2.ROTATE_180}

print("flip rotate 90 clockwise: ", flip["ROTATE_90_CLOCKWISE"])

for key, value in flip.items():
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("original")
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(cv2.rotate(image, value), cv2.COLOR_BGR2RGB))
    plt.title(key) 
    plt.show()
    # Save plt to image and save image
    plt.savefig(key + ".png")
    plt.close()

print("Cropping images")

UPPER = 150
LOWER = 400
crop_top = image[UPPER:LOWER, :, :]
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(crop_top, cv2.COLOR_BGR2RGB))
plt.show()

LEFT = 150
RIGHT = 400
crop_horizontal = crop_top[:, LEFT:RIGHT, :]
plt.figure(figsize=(5, 5))
plt.imshow(cv2.cvtColor(crop_horizontal, cv2.COLOR_BGR2RGB))
plt.show()

array_sq = np.copy(image)
array_sq[UPPER:LOWER, LEFT:RIGHT, :] = 0

plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("original")
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(array_sq, cv2.COLOR_BGR2RGB))
plt.title("Altered Image")
plt.show()

start_point, end_point = (LEFT, UPPER), (RIGHT, LOWER)
image_draw = np.copy(image)
cv2.rectangle(image_draw, pt1=start_point, pt2=end_point, color=(0, 255, 0), thickness=3)
plt.figure(figsize=(5, 5))
plt.imshow(cv2.cvtColor(image_draw, cv2.COLOR_BGR2RGB))
plt.show()

print("Overlay Text")
image_draw = cv2.putText(img=image, text='Stuff', org=(10, 500), color=(255, 255, 255), fontFace=4, fontScale=5, thickness=2)
plt.figure(figsize=(10, 10))    
plt.imshow(cv2.cvtColor(image_draw, cv2.COLOR_BGR2RGB))
plt.show()

# write your code here
im = cv2.imread("baboon.png")
#convert from bgr to rgb
im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

im_flip = cv2.flip(im, 0)
im_mirror = cv2.flip(im, 1)

#plot both images

#flip
plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(im,cv2.COLOR_BGR2RGB))
plt.title("orignal")
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(im_flip,cv2.COLOR_BGR2RGB))
plt.title("flip Image") 
#mirror
plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(im,cv2.COLOR_BGR2RGB))
plt.title("orignal")
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(im_mirror,cv2.COLOR_BGR2RGB))
plt.title("mirror Image") 

plt.show()
print("End of line....")