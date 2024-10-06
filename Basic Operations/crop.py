import cv2 as cv


# crop
img = cv.imread('Photos/park.jpg')
cv.imshow('Park',img)



crop_img = img[0:600 , 0:200]
cv.imshow("Crop Image",crop_img)


cv.waitKey(0)