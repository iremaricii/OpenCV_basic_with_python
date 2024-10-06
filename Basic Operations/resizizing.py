import cv2 as cv


# resizing
img = cv.imread('Photos/park.jpg')
dimensions_one = img.shape
cv.imshow(f'Park {dimensions_one}', img)



resized_img = cv.resize(img, (200, 320))
dimensions_two = resized_img.shape
cv.imshow(f'Resized Park Image {dimensions_two}', resized_img)



cv.waitKey(0)