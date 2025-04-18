import matplotlib.pyplot as plt
import cv2

img = cv2.imread("photo4.jpg")
b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])
img_copy = img.copy()

plt.subplot(331)
plt.imshow(img)
pointA = (975,1707)
pointB = (1777,1990)

img2 = cv2.line(img.copy(),pointA,pointB,(255,255,0),30,cv2.LINE_AA)
plt.subplot(332)
plt.imshow(img2)

circle_centre = (3000,1972)

img3 = cv2.circle(img.copy(),circle_centre,500,(0,255,255),30)
plt.subplot(333)
plt.imshow(img3)

img4 = cv2.rectangle(img.copy(),pointA,pointB,(255,0,255),30)
plt.subplot(131)
plt.imshow(img4)

img5 = cv2.ellipse(img.copy(),(1692,1565),(500,180),180,0,360,(255,0,0),50)
plt.subplot(132)
plt.imshow(img5)

org = (1051,1900)
text = "11 II 111"
img6 = cv2.putText(img.copy(),text,org,cv2.FONT_HERSHEY_COMPLEX,4.0,(0,0,0),10)
plt.subplot(133)
plt.imshow(img6)
plt.show()