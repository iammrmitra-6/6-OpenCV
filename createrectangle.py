import cv2
import numpy as np

img = np.zeros((512, 512, 3), dtype=np.uint8)
drawing = False
start_x = start_y = 0


def draw(event, x, y, flags, params):
    global drawing, start_x, start_y, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp = img.copy()
            cv2.rectangle(temp, (start_x, start_y), (x, y), (0, 255, 0), 2)
            cv2.imshow("window", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (start_x, start_y), (x, y), (0, 255, 0), 2)


cv2.namedWindow("window")
cv2.setMouseCallback("window", draw)

while True:
    cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
