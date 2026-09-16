import cv2
import numpy as np

img = np.zeros((512, 512, 3), dtype=np.uint8)


def draw(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (0, 0, 255), -1)


cv2.namedWindow("window")
cv2.setMouseCallback("window", draw)

while True:
    cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
