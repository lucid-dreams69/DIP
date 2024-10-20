import cv2
img =  cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/itachi flowers.jpeg",cv2.IMREAD_UNCHANGED)
print('Original Dimension:',img.shape)
cv2.imshow('Original Image',img)

scalingfactor = 0.5
width = int(img.shape[1]*scalingfactor)
height = int(img.shape[0]*scalingfactor)
dim = (width,height)
img1 = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
print('Resized Dimensions after downscaling:',img1.shape)
cv2.imshow("Downscale Image",img1)

scalingfactor = 1.5
width = int(img.shape[1]*scalingfactor)
height = int(img.shape[0]*scalingfactor)
dim = (width,height)
img2 = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
print('Resized Dimensions after upscaling:',img2.shape)
cv2.imshow("Upscale Image",img2)

width = 440
height = img.shape[0]
dim = (width,height)
img3 = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
print('Resized only width:',img3.shape)
cv2.imshow("Resized only width",img3)

width = img.shape[1]
height = 440
dim = (width,height)
img4 = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
print('Resized only height:',img4.shape)
cv2.imshow("Resized only height",img4)

width = 350
height = 450
dim = (width,height)
img5 = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
print('Resize to specific width and height:',img5.shape)
cv2.imshow("Resize to specific width and height",img5)

cv2.waitKey(0)
cv2.destroyAllWindows()