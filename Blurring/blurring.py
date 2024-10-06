import cv2 as cv


# Blurring
img = cv.imread('Photos/lady.jpg')

k_size = 7
img_blur = cv.blur(img[60:558,76:522], (k_size, k_size))
img_gaussian_blur = cv.GaussianBlur(img[60:558,76:522], (k_size, k_size),3)
img_median_blur = cv.medianBlur(img[60:558,76:522], (k_size))

cv.imshow('Lady',img)
cv.imshow('Lady Blurring',img_blur)
cv.imshow('Lady Gaussian Blurring',img_gaussian_blur)
cv.imshow('Lady Median Blurring',img_median_blur)

cv.waitKey(0)