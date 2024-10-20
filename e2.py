import cv2
i1=cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/SUNITHA/anime-girl-5wx (2).png")
cv2.imshow('Original Image',i1)
i2 = i1.copy()

A = (50,100)
B = (300,100)
cv2.line(i2,A,B,(255,255,0),thickness=3)
cv2.imshow('Image Annotated with Line',i2)

i3 = i1.copy()
center = (100, 80)
radius =10
cv2.circle(i3,center,radius,(255,255,0),thickness=1,lineType=cv2.LINE_AA)
cv2.imshow('Image Annotated with circle',i3)

i4 = i1.copy()
cv2.circle(i4,center,radius,(255,255,0),thickness=-1,lineType=cv2.LINE_AA)
cv2.imshow('Image Annotated with Filled circle',i4)

i5 = i1.copy()
a =(60,60)
b =(170,120)
cv2.rectangle(i5,a,b,(255,255,0),thickness=3,lineType=cv2.LINE_8)
cv2.imshow('Image Annotated with Rectangle',i5)

i6 = i1.copy()
center = (130,90)
axis1 = (100,50)
axis2 = (125,50)
cv2.ellipse(i6,center,axis1,0,0,360,(255,255,0),thickness=3)
cv2.ellipse(i6,center,axis2,90,0,360,(255,255,0),thickness=3)
cv2.imshow('Image Annotated with Ellipse',i6)

i7 = i1.copy()
center = (130,90)
axis1 = (100,50)
cv2.ellipse(i7,center,axis1,0,180,360,(255,0,0),3,8,0)
cv2.ellipse(i7,center,axis1,0,0,180,(255,255,0),-2,8,0)
cv2.imshow('Image Annotated with Half Ellipse',i7)
cv2.waitKey(0)
cv2.destroyAllWindows()