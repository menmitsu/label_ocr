# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np

# Reading the input image
img = cv2.imread('label.jpg', 0)

cv2.imshow('Input',img)
cv2.imwrite("output.jpg",img)

# Taking a matrix of size 5 as the kernel
kernel = np.ones((5,5), np.uint8)

# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
# img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

edges = cv2.Canny(image=img_dilation, threshold1=50, threshold2=100) # Canny Edge Detection


kernel = np.array([[0, -1, 0],
                   [-1, 7,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=img_dilation, ddepth=-1, kernel=kernel)

#cv2.imshow('Input', img)
# cv2.imshow('Erosion', img_erosion)

cv2.imshow('Dilation', img_dilation)
cv2.imshow('Canny',edges)
cv2.imshow('sharp',image_sharp)
cv2.imwrite("output.jpg",img_dilation)
cv2.imwrite("output_canny.jpg",edges)
cv2.imwrite("output_sharp.jpg",image_sharp)

cv2.waitKey(0)
