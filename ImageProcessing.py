from PIL import Image
from pytesseract import pytesseract
import cv2
import numpy as np

image_path = r"Money\test.png"

img = cv2.imread(image_path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

white_lo = np.array([0, 0, 255])
white_hi = np.array([0, 0, 255])

# Mask image to only select browns
mask = cv2.inRange(hsv, white_lo, white_hi)

# Change image to black where we found brown
img[mask>0]=(255,255,255)

invert_img = cv2.bitwise_not(mask)

cv2.imwrite(r"Money/result1.png", invert_img)


# Apply threshold to convert to binary image
# threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# invert_img = cv2.bitwise_not(threshold_img)

# cv2.imwrite(r'Money/grayScale.png', gray)
# cv2.imwrite(r'Money/threshold.png', threshold_img)
# cv2.imwrite(r'Money/invert.png', invert_img)
# print(hsv)
# cv2.imwrite(r'Money/HsvScale.png', hsv)