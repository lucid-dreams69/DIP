import cv2
import numpy as np
img = cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/purple.jpeg")
contrast_img = cv2.addWeighted(img,1,np.zeros(img.shape,img.dtype),0,100)
cv2.imshow('Original Image',img)
cv2.imshow('Contrast Image',contrast_img)
cv2.waitKey(0)