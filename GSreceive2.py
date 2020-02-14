import cv2
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('udp://10.0.0.218:1994?overrun_nonfatal=1&fifo_size=50000000?buffer_size=10000000', cv2.CAP_FFMPEG)
cap = cv2.VideoCapture('udp://192.168.1.30:1235?overrun_nonfatal=1&fifo_size=50000000?buffer_size=10000000', cv2.CAP_FFMPEG)
if not cap.isOpened():
    print('VideoCapture not opened')
    exit(-1)
# cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image', 1280, 720)
while True:
    ret, frame = cap.read()
    if not ret:
        print('frame empty')
        break
    # frameResize = cv2.resize(frame, (720, 480))
    cv2.imshow('image2', frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()