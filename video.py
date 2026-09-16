import cv2


cap = cv2.VideoCapture(0)

out = None

try:
	while True:
		ret, frame = cap.read()
		if not ret:
			break

		if out is None:
			height, width = frame.shape[:2]
			fourcc = cv2.VideoWriter_fourcc(*'mp4v')
			out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))
			if not out.isOpened():
				raise RuntimeError("Could not open output.mp4 for writing")

		out.write(frame)

		cv2.imshow("webcam", frame)

		if cv2.waitKey(1) & 0xFF == ord('x'):
			break
finally:
	cap.release()
	if out is not None:
		out.release()
	cv2.destroyAllWindows()