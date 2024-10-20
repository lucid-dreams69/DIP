import cv2

import numpy as np
import matplotlib.pyplot as pit

img = cv2.imread("C:/Users/USER/OneDrive/Pictures/Saved Pictures/itachi flowers.jpeg",0)
his_1 = cv2.calcHist([img],[0],None,[256],[0,256])
plt.title("HISTOGRAM OF ORIGINAL IMAGE")
plt.xlable('INTENSITY')
plt.ylable('NO.OF.PIXELS')
plt.plot(his_1)
plt.show()
img_1 = cv2.equalizeHist(img)
hist_2 cv2