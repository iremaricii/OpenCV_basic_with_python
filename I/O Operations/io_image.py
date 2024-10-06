import cv2 as cv


# read image
img = cv.imread('Photos/group 1.jpg')

# visualize image
cv.imshow('Group',img)

cv.waitKey(0)