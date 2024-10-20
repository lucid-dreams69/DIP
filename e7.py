import cv2
img1=cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/images (3).jpeg")
img2=cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/images.jpeg")

result1 = cv2.add(img1,img2)

cv2.imshow('First Image',img1)
cv2.imshow('secend Image',img2)
cv2.imshow('Addition - Final Image',result1)

result2 = cv2.subtract(img2,img1)
cv2.imshow('Subtraction - Final Image',result2)

result3 = cv2.addWeighted(img1,0.2,img2,0.8,0)
cv2.imshow('Blending - Final Image',result3)

result4 = cv2.bitwise_and(img2,img1,mask= None)
cv2.imshow('Bitwise-AND - Final Image',result3)

result5 = cv2.bitwise_or(img2,img1,mask= None)
cv2.imshow('Bitwise-OR- Final Image',result5)

result6 = cv2.bitwise_xor(img2,img1,mask= None)
cv2.imshow('Bitwise-XOR- Final Image',result6)

result7 = cv2.bitwise_not(img2,mask= None)
cv2.imshow('Bitwise-NOT- Final Image',result7)

cv2.waitKey(0)
cv2.destroyAllWindows()