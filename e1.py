import cv2
i1=cv2.imread("D:/ost/123.jpeg")
cv2.imshow('Original Image',i1)
i2=cv2.imread("D:/ost/123.jpeg",0)
cv2.imshow('Grayscale Image',i2)

i3 = cv2.copyMakeBorder(i1,200,20,120,20,cv2.BORDER_CONSTANT,value = 0)
cv2.imshow('Image with Border',i3)
i4 = cv2.copyMakeBorder(i1,20,20,20,20,cv2.BORDER_CONSTANT,value = 100)
cv2.imshow('Image with Blue Colored Border',i4)
i5 = cv2.copyMakeBorder(i1,20,20,20,20,cv2.BORDER_CONSTANT,value = [203, 192, 255])
cv2.imshow('Image with  Green Colored  Border',i5)
i6 = cv2.copyMakeBorder(i1,20,20,20,20,cv2.BORDER_CONSTANT,value = [0, 0, 225])
cv2.imshow('Image with  Red Colored  Border',i6)

i7 = i1[80:280, 150:330]
cv2.imshow('Cropped Image',i7)
cv2.imwrite('Grayscale Image.jpg',i7)

i8=i1.copy()
cv2.putText(img=i8,text='Hiii welcome',org=(50,50),fontFace=cv2.FONT_HERSHEY_TRIPLEX,
fontScale=2,color=(255,0,0),thickness=2)
cv2.imshow('Image with text',i8)

cv2.waitKey(0)
cv2.destroyAllWindows()