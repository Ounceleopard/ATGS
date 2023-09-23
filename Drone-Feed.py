import cv2
import requests
import numpy as np

# Replace with the actual IP and port of your homebase server
homebase_server_ip = "your_homebase_server_ip"
homebase_server_port = "your_homebase_server_port"

# Capture video from the remote camera (use 0 for the default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Encode the frame as JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    frame_bytes = buffer.tobytes()

    # Send the frame to the homebase server
    try:
        response = requests.post(
            f"http://{homebase_server_ip}:{homebase_server_port}/upload",
            data=frame_bytes,
            headers={'Content-Type': 'image/jpeg'}
        )
    except requests.exceptions.RequestException as e:
        print(f"Error sending frame to server: {e}")

cap.release()


" Target Tracking 

import cv2
import numpy as np

# Load YOLOv3 configuration and weights
yolo_net = cv2.dnn.readNet("yolov3.cfg", "yolov3.weights")

# Load COCO class names
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Set up video capture from your drone or a video file
cap = cv2.VideoCapture(0)  # Change to the video file path if needed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Get height and width of the frame
    height, width = frame.shape[:2]

    # Prepare the frame for YOLO object detection
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    yolo_net.setInput(blob)

    # Run YOLO object detection
    detections = yolo_net.forward("yolov3")

    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and classes[class_id] == "person":
                # Object is a person with confidence > 0.5
                center_x = int(obj[0] * width)
                center_y = int(obj[1] * height)
                w = int(obj[2] * width)
                h = int(obj[3] * height)

                # Calculate the coordinates of the bounding box
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Draw bounding box and label
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Person", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame with bounding boxes
    cv2.imshow("Human Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
