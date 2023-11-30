import cv2
from pyzbar.pyzbar import decode
import time

video_file_path = ''
cap = cv2.VideoCapture(video_file_path)

if not cap.isOpened():
    print(f"Error: Could not open video file '{video_file_path}'")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to read a frame from the video")
        break

    start_time = time.time()
    decoded_objects = decode(frame)
    end_time = time.time()
    detection_time = end_time - start_time

    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        cv2.putText(frame, data, (obj.rect.left, obj.rect.top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
                      (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height), (0, 255, 0), 2)
        print(f"Детекция заняла {detection_time} секунд")
        print(data)

    cv2.imshow('Barcode Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
