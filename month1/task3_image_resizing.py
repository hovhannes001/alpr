import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

img = cv2.imread("photo1.png")
down_width = 100
down_height = 200

resized_down = cv2.resize(img,(down_width,down_height),interpolation = cv2.INTER_LINEAR)

# img = cv2.imread("photo1.png")
up_width = 600
up_height = 900

resized_up = cv2.resize(img,(up_width,up_height),interpolation = cv2.INTER_LINEAR)


cv2.imshow("resized_down",resized_down)
cv2.waitKey(0)
cv2.imshow("resized up",resized_up)
cv2.waitKey(0)
cv2.destroyAllWindows()

scale_up = 1.2
scale_down = 0.1

resized_scale__down = cv2.resize(img,None,fx=scale_down,fy=scale_down,interpolation = cv2.INTER_LINEAR)
resized_scale__up = cv2.resize(img,None,fx = scale_up,fy = scale_down,interpolation= cv2.INTER_LINEAR)
res_inter_nearest = cv2.resize(img, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_NEAREST)
res_inter_linear = cv2.resize(img, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)
res_inter_area = cv2.resize(img, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_AREA)
cv2.imshow("resized_down",resized_scale__down)
cv2.waitKey()
cv2.imshow("resized up", resized_scale__up)
cv2.waitKey()

vertical= np.concatenate((res_inter_nearest, res_inter_linear, res_inter_area), axis = 1)

cv2.imshow('Inter Nearest :: Inter Linear :: Inter Area', vertical)
cv2.waitKey()

# img = cv2.imread("photo2.webp")
# rows,cols,ch = img.shape
 
# pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
# pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
 
# M = cv2.getPerspectiveTransform(pts1,pts2)
 
# dst = cv2.warpPerspective(img,M,(300,300))
 
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()