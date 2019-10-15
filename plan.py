# imports
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import gridspec

# read and display the image as a reference
img = cv2.imread('images/fruits.png')
# cv2.imshow('Fruit Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

height, width, channels = img.shape[:3]
print('Image height: {}, Width: {}, # of channels: {}'.format(height, width, channels))

blues = img[:, :, 0]
greens = img[:, :, 1]
reds = img[:, :, 2]

# cv2.imshow('Fruit Blues', blues)
# cv2.imshow('Fruit Greens', greens)
# cv2.imshow('Fruit Reds', reds)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plot values for each color plane on a specific row
fig = plt.figure(figsize=(10, 4))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])

# original image
ax0 = plt.subplot(gs[0])
ax0.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # need to convert BGR to RGB
ax0.axhline(50, color='black') # show the row being used
ax0.axvline(100, color='k'), ax0.axvline(225, color='k') # ref lines
# image slice
ax1 = plt.subplot(gs[1])
ax1.plot(blues[49, :], color='blue')
ax1.plot(greens[49, :], color='green')
ax1.plot(reds[49, :], color='red')
ax1.axvline(100, color='k', linewidth=2), ax1.axvline(225, color='k', linewidth=2)

plt.suptitle('Examen des valeurs du plan de couleur pour une seule ligne')
plt.show()

img = cv2.imread('images/b1.jpg')

cropped = img[109:310, 9:160]
cv2.imshow('Cropped Image', cropped)
print ("press 's' to save the image as cropped_bicycle.png\n")
key = cv2.waitKey(0) # if you are using a 64-bit machine see below
# the above line should be: key = cv2.waitKey(0) & 0xFF
if key == 27: # wait for the ESC key to exit
    cv2.destroyAllWindows()
elif key == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('images/cropped_bicycle.png', img)
    cv2.destroyAllWindows()
 # get the size of the cropped image
height, width = cropped.shape[:2]
print ('Cropped Width: {}px, Cropped Height: {}px'.format(width, height))

x = np.uint8([250])
y = np.uint8([10])
print ('Open CV Addition {}'.format(cv2.add(x, y))) # 250+10 = 260 => 255
print ('')
print ('Numpy Addition {}\n'.format(x+y)) # 250+10 = 260 % 256 = 4

# if bicycle.shape[:2] == dolphin.shape[:2]:
#     sum_img = cv2.add(bicycle, dolphin) # add images together
#     cv2.imshow('Summed Images', sum_img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     scaled_img = cv2.add(bicycle, 50)     cv2.imshow('Scalar Addition on Bicycle Image', scaled_img)     cv2.waitKey(0)     cv2.destroyAllWindows()