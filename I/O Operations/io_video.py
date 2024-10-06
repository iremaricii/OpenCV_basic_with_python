import cv2 as cv

# read video
video = cv.VideoCapture('Videos/kitten.mp4')



ret = True
while ret:
    # ret isframe : true or false
    ret, frame = video.read()
    cv.imshow('Kitten',frame)
    if cv.waitKey(40) & 0xFF == ord('q'):
        break
        
video.release() # When you're done, release the video source.
cv.destroyAllWindows()