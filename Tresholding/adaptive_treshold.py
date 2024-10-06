import cv2 as cv

img = cv.imread('Photos/handwritten.png')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

adaptive_thresh = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, 30)
ret, simple_thresh = cv.threshold(img_gray, 80, 255, cv.THRESH_BINARY)


cv.imshow('img', img)
cv.imshow('adaptive_thresh', adaptive_thresh)
cv.imshow('simple_thresh', simple_thresh)
cv.waitKey(0)