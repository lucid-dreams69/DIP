import cv2

import numpy as np

img = cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/purple.jpeg")

cv2.imshow('Original Image',img)

L = img.max()
img_neg = L-1-img
cv2.imshow('Negative Image',img_neg)
np.seterr(divide = 'ignore')

c = 255/(np.log(1 + np.max(img))) 

img_log = c*np.log(1 + img)
img_log = np.array(img_log,dtype= np.uint8)

cv2.imshow('log_transformed',img_log)
for gamma in [-1,0.1,0.5,1.2,2.2,3.5]:
    img_power = np.array(255*(img/255)**gamma,dtype = 'uint8')
    cv2.imshow('Gamma ='+str(gamma),img_power)
cv2.waitKey(0)
cv2.destroyAllWindows()