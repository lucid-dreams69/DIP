import cv2
import numpy
i1 = cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/itachi flowers.jpeg")
cv2.imshow('Original Image',i1)

b,g,r = cv2.split(i1)
cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red',r)

zeros = numpy.zeros(b.shape,numpy.uint8)
blue = cv2.merge((b,zeros,zeros))
green = cv2.merge((zeros,g,zeros))
red = cv2.merge((zeros,zeros,r))
cv2.imshow('Blue Channel',blue)
cv2.imshow('Green Channel',green)
cv2.imshow('Red Channel',red)
i2=cv2.merge([b,g,r])
cv2.imshow('BGR MERGED IMAGE',i2)

i3 = cv2.cvtColor(i1,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image',i3)
h,s,v = cv2.split(i3)
cv2.imshow('H Channel',h)
cv2.imshow('S Channel',s)
cv2.imshow('V Channel',v)

i4=cv2.merge([h,s,v])
cv2.imshow('HSV MERGED IMAGE',i4)
cv2.waitKey(0)
cv2.destroyAllWindows()
