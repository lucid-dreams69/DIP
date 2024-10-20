import cv2

i1=cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/itachi flowers.jpeg")
cv2.imshow('Original Image',i1)

i2 = cv2.cvtColor(i1,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image',i2)

i3 = cv2.cvtColor(i1,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image',i3)

i4 = cv2.cvtColor(i1,cv2.COLOR_BGR2RGB)
cv2.imshow('RGB Image',i4)

i5 = cv2.cvtColor(i1,cv2.COLOR_BGR2LAB)
cv2.imshow('LAB Image',i5)

i6 = cv2.cvtColor(i1,cv2.COLOR_BGR2YUV)
cv2.imshow('YUV Image',i6)

i7 = cv2.cvtColor(i1,cv2.COLOR_BGR2YCrCb)
cv2.imshow('YCrCb Image',i7)

i8 = cv2.cvtColor(i1,cv2.COLOR_BGR2BGRA)
cv2.imshow('BGRA Image',i8)

i9 = cv2.cvtColor(i1,cv2.COLOR_BGR2LUV)
cv2.imshow('LUV Image',i9)

cv2.waitKey(0)
cv2.destroyAllWindows()