import cv2
import numpy 
img = cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/purple.jpeg")
cv2.imshow('Original Image',img)

print(" ACCESSING PIXEL VALUES OF A COLORED IMAGE ")
px = img[50,50]
print("The pixel value:",px)

blue = img[50,50,0]
print("The value of blue for the current pixel:",blue)
green = img[50,50,1]
print("The value of green for the current pixel:",green)
red = img[50,50,2]

print("The value of red for the current pixel:",red)
print("")
print(" ACCESSING IMAGE PROPERTIES OF A COLORED IMAGE ")
print("Image Size:",img.shape)
print("Image Height:",img.shape[0])
print("Image Width:",img.shape[1])
print("Number of channels:",img.shape[2])
print("Total number of pixels:",img.size)
print("Image Datatype:",img.dtype)

img1 = cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/purple.jpeg",0)
cv2.imshow("Gray Scale Image",img1)

print("")
print(" ACCESSING PIXEL VALUES OF A GRAY SCALE IMAGE ")
px1 = img1[100,100]
print("The pixel value:",px1)
print("")
print(" ACCESSING IMAGE PROPERTIES OF A GRAY SCALE IMAGE ")
print("Image Size:",img1.shape)
print("Image Height:",img1.shape[0])
print("Image Width:",img1.shape[1])
print("Total number of pixels:",img1.size)
print("Image Datatype:",img1.dtype)
cv2.waitKey(0)
cv2.destroyAllWindows()