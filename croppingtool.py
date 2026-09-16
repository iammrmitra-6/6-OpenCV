import cv2
import numpy as np

img = cv2.imread("aeroplane.png")
if img is None:
    raise FileNotFoundError("aeroplane.png not found in the current folder.")

img_copy = img.copy()
start_x = start_y = -1
drawing = False
cropped = None


def draw_rectangle(event, x, y, flags, param):
    global img_copy, start_x, start_y, drawing, cropped

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y
        img_copy[:] = img[:]

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp = img.copy()
            cv2.rectangle(temp, (start_x, start_y), (x, y), (0, 255, 0), 2)
            cv2.imshow("Crop Tool", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        if drawing:
            drawing = False
            x1, y1 = min(start_x, x), min(start_y, y)
            x2, y2 = max(start_x, x), max(start_y, y)
            cropped = img[y1:y2, x1:x2]
            cv2.rectangle(img_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.imshow("Crop Tool", img_copy)
            cv2.imwrite("cropped_airplane.png", cropped)
            print("Cropped image saved as cropped_airplane.png")
            print("Cropped size:", cropped.shape)


cv2.namedWindow("Crop Tool")
cv2.setMouseCallback("Crop Tool", draw_rectangle)
cv2.imshow("Crop Tool", img)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('x'):
        break
    if key == ord('s') and cropped is not None:
        cv2.imwrite("cropped_airplane.png", cropped)
        print("Saved cropped image as cropped_airplane.png")

cv2.destroyAllWindows()
