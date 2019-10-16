# library imports
import cv2.cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Chargement d'une image
image = cv.imread('images/dolphin.png', 0)
cv.imshow('Input', image)

# Histogramme
#histogramme = cv.calcHist([image], [0], None, [256], [0, 256])
plt.hist(image.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
