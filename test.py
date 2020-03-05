# file: test.py
import cv2
import time
from videocaptureasync import VideoCaptureAsync

def test(n_frames=500, width=1280, height=720, asynca=False):
    if asynca:
        cap = VideoCaptureAsync(0)
    else:
        cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    if asynca:
        cap.start()
    t0 = time.time()
    i = 0
    while i < n_frames:
        ret, frame = cap.read()
        print(frame)
        if ret:
            cv2.imshow('Frame', frame)
        cv2.waitKey(1) & 0xFF
        i += 1
    print('[i] Frames per second: {:.2f}, asynca={}'.format(n_frames / (time.time() - t0), asynca))
    if asynca:
        cap.stop()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    test(n_frames=5, width=1280, height=720, asynca=False)
    test(n_frames=5, width=1280, height=720, asynca=True)