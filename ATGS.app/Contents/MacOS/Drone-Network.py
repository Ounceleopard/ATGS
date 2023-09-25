# pip install opencv-python-headless

import cv2

# Replace with the actual RTMP stream URL
rtmp_stream_url = "rtmp://your_rtmp_server_ip/live/your_stream_key"

cap = cv2.VideoCapture(rtmp_stream_url)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video Feed", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

