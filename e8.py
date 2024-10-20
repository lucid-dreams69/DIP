import cv2
import numpy as np
img = cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/purple.jpeg")
height,width=img.shape[0:2]
tx = input("Enter the translation distance along x-axis:")
ty = input("Enter the translation distance along y-axis:")
M = np.float32([[1,0,tx],[0,1,ty]])
img_tran = cv2.warpAffine(img,M,(width,height))
result = np.hstack((img,img_tran))
cv2.imshow('ORIGINAL IMAGE vs TRANSLATED IMAGE',result)
img = cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/SUNITHA/anime-girl-5wx (2).png")
height,width = img.shape[0:2]
angle=input("Emter the angle of rotation:")
RotationMatrix = cv2.getRotationMatrix2D((width/2,height/2),int(angle),1)
img_rot=cv2.warpAffine(img,RotationMatrix,(width,height))
result = np.hstack((img,img_rot))
cv2.imshow('ORIGINAL IMAGE vs ROTATED IMAGE',result)
cv2.waitKey(0)
cv2.destroyAllWindows()