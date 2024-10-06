import cv2 as cv


img = cv.imread('Photos/bear.jpg')

img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret, img_treshold = cv.threshold(img_gray, 80, 255, cv.THRESH_BINARY)
img_treshold= cv.blur(img_treshold, (10,10))
ret, img_treshold = cv.threshold(img_treshold, 80, 255, cv.THRESH_BINARY)

cv.imshow('Lady',img)
cv.imshow('Lady GRAY',img_gray)
cv.imshow('Lady Treshold',img_treshold)
cv.imshow('Lady blur',img_treshold)
cv.waitKey(0)