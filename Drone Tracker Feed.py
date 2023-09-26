import cv2
import socket
import sys
import pickle
import struct

# Set the IP address and port for the server (client program will use this to connect)
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

# Create a socket to send data
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    sender_socket.connect((SERVER_IP, SERVER_PORT))
    print(f"Connected to {SERVER_IP}:{SERVER_PORT}")

    # Initialize the video capture from the drone (use appropriate camera index or URL)
    drone_camera = cv2.VideoCapture(0)  # Change 0 to your camera index or URL
    drone_camera.set(cv2.CAP_PROP_FPS, 30)  # Set the desired frame rate
    drone_camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    drone_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    """
1920 x 1080 HD
1280 x 720 HD
640 x 480 VGA
320 x 240 QVGA
    """

    # https://www.ijraset.com/research-paper/different-tracking-algorithms-in-opencv
    # Initialize the KCF tracker Pros: Accuracy and speed are both better than MIL and it reports tracking failure better than BOOSTING and MIL.
    """
    tracker = cv2.TrackerKCF_create()
    """
    # tracker = cv2.TrackerMIL_create()
    tracker = cv2.TrackerMIL_create()

    # Initialize variables to store the initial bounding box coordinates
    bbox = None
    tracking = False

    while True:
        # Capture a frame from the drone camera
        ret, frame = drone_camera.read()

        # If we are not tracking, display the frame and wait for the user to select a bounding box
        if not tracking:
            cv2.imshow("Drone Camera", frame)
            key = cv2.waitKey(1) & 0xFF

            # Press 's' to select a bounding box to track
            if key == ord("s"):
                bbox = cv2.selectROI("Drone Camera", frame, fromCenter=False, showCrosshair=True)
                tracker.init(frame, bbox)
                tracking = True

        # If we are tracking, update the tracker and get the new bounding box
        if tracking:
            # Update the tracker and get the new bounding box
            success, bbox = tracker.update(frame)

            if success:
                # Tracking successful, draw the bounding box
                (x, y, w, h) = [int(v) for v in bbox]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Serialize the frame using pickle
        data = pickle.dumps(frame)

        # Pack the frame size and data into a struct
        message = struct.pack('Q', len(data)) + data

        # Send the frame to the client
        sender_socket.sendall(message)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    if 'drone_camera' in locals() and drone_camera.isOpened():
        drone_camera.release()
    sender_socket.close()


