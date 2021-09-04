import argparse
import base64
import time
import time

import cv2
import numpy as np
import requests

import imutils
from imutils.object_detection import non_max_suppression

# OpenCV pre-trained SVM with HOG people features
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detector(image):
    """
    @image is a numpy array
    """

    clone = image.copy()

    (rects, weights) = HOGCV.detectMultiScale(
        image, winStride=(4, 4), padding=(8, 8), scale=1.05
    )

    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Applies non-max supression from imutils package to kick-off overlapped
    # boxes
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    result = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    return result


def send_results(count):
    print(count)


def camera_detect():
    cap = cv2.VideoCapture(0)
    init = time.time()
    sample_time = 5

    if sample_time < 1:
        sample_time = 1

    while True:
        # Capture frame-by-frame
        _, frame = cap.read()
        frame = imutils.resize(frame, width=min(400, frame.shape[1]))
        result = detector(frame.copy())

        # shows the result
        for (xA, yA, xB, yB) in result:
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
        cv2.imshow("frame", frame)

        # Sends results
        if time.time() - init >= sample_time:
            print("[INFO] Sending actual frame results")
            send_results(len(result))
            init = time.time()

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


def main():
    camera_detect()


if __name__ == "__main__":
    main()
