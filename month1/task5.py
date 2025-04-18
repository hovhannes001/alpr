import matplotlib.pyplot as plt
import cv2

img = cv2.imread("photo2.webp")
b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])
height,width = img.shape[:2]
plt.subplot(131)
plt.imshow(img)
center = (width /2 , height / 2)
rotadet_matrix = cv2.getRotationMatrix2D(center = center, angle= 9, scale= 1)

rotated_image = cv2.warpAffine(img,rotadet_matrix,(width,height))

plt.subplot(132)
plt.imshow(rotated_image)


import numpy as np

tx = 50
ty = 100

translation_matrix = np.float32(
    [[1, 0, tx],
     [0, 1, ty]]
)

translated_image = cv2.warpAffine(img,translation_matrix,(img.shape[1],img.shape[0]))

plt.subplot(133)
plt.imshow(translated_image)
plt.show()