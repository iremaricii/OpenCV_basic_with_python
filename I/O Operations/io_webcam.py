import cv2 as cv

# read webcam

webcam = cv.VideoCapture(0)

# visualize webcam
while  True:
    ret, frame = webcam.read()
    cv.imshow('WEBCAM',frame)
    if cv.waitKey(40) & 0xFF == ord('q'):
        break
        
       

webcam.release()
cv.destroyAllWindows()