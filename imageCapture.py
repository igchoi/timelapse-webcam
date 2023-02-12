import numpy as np
import cv2 as cv
import schedule
import time

cap = cv.VideoCapture(0)
# Set properties
# https://stackoverflow.com/questions/57660458/cant-set-frame-width-and-height-with-opencv-cv2-videocapture-set
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
print('original size: %d, %d' % (width, height))

if not cap.isOpened():
    print("Cannot open camera")
    exit()

img_counter = 0
t0 = time.time()

while True:
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)  # only fixed resolution in a webcam??
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    # print('changed size: %d, %d' % (width, height))
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)  # 'frame' is window 'name'
    # https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv
    if cv.waitKey(1) == ord('q'):
        break
    #    elif cv.waitKey(1) == ord('s'):
    else:
        t1 = time.time()
        if (t1 - t0) >= 5.0:
            img_counter += 1
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            t0 = t1


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
