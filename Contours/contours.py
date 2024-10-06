import cv2 as cv


img = cv.imread('Photos/birds.jpg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv.contourArea(cnt) > 200:
        # cv.drawContours(img, cnt, -1, (0, 255, 0), 1)

        x1, y1, w, h = cv.boundingRect(cnt)

        cv.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

cv.imshow('img', img)
cv.imshow('thresh', thresh)
cv.waitKey(0)