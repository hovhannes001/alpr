import matplotlib.pyplot as plt
import cv2

img = cv2.imread("photo3.jpg", cv2.IMREAD_UNCHANGED)
b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])

cropped_img = img[24:190, 100:190]
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(cropped_img)
plt.show()

