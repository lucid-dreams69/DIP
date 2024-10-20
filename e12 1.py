import cv2

import numpy as np

img = cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/itachi flowers.jpeg")

cv2.imshow('ORIGINAL ',img)
img1 = cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/itachi flowers.jpeg",0)
cv2.imshow("Gray Scale",img1)
r,c = img1.shape
x = np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    x[:,:,i] = 2**i
r = np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    r[:,:,i] = cv2.bitwise_and(img1,x[:,:,i])
    mask=r[:,:,i]>0
    r[mask]=255
    cv2.imshow('plane'+str(i),r[:,:,i])
cv2.waitKey(0)
cv2.destroyAllWindows()