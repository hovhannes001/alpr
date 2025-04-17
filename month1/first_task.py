import cv2
import matplotlib.pyplot as plt
img = cv2.imread("./logo.png")
print(type(img))
total_number_of_elements = img.shape
dimensions = img.size

img2 = cv2.imread("roi.jpg")
# img[6,6] = (0,0,0)
# cv2.imshow("messi",img)  
# cv2.waitKey(0)
gray_img = cv2.imread("logo.png",cv2.IMREAD_GRAYSCALE)
dimensions_gray = gray_img.shape
gray_img_size = gray_img.size
b,g,r = cv2.split(img)
mathplotlib_img = cv2.merge([r,g,b])
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(mathplotlib_img)
plt.show()
cv2.imwrite("test.jpg",mathplotlib_img)
cv2.destroyAllWindows()
