import cv2 as cv

#Colorspaces
img = cv.imread('Photos/lady.jpg')

# convert bgr to rgb
img_rgb = cv.cvtColor(img, cv.COLOR_BGRA2RGB)
# convert to bgr to gray
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)



cv.imshow('Lady', img)
cv.imshow('Lady RGB', img_rgb)
cv.imshow('Lady Gray',img_gray)
cv.imshow('Lady HSV',img_hsv)
cv.waitKey(0)

