import cv2
import numpy as np
img = cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/purple.jpeg")
bright_img = cv2.addWeighted(img,1,np.zeros(img.shape,img.dtype),0,205)
cv2.imshow('Brightened Image',bright_img)
cv2.waitKey(0)