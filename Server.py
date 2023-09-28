# Server: Takes and displays the feed from the drone

import cv2
import socket
import pickle
import struct
import numpy as np
import time

# Define the server IP address and port
server_ip = '127.0.0.1'  # Change this to your desired IP address
server_port = 8080  # Change this to your desired port number

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)  # 5 Different clients can connect.

print("Server is listening for incoming connections...")

try:
    client_socket, addr = server_socket.accept()
    print(f"Drone feed connection established from {addr}.")
    disconnected = False

    fps = 0
    frame_counter = 0
    start_time = time.time()

    resolution = ""  # Initialize resolution here

    while True:
        data = b''
        payload_size = struct.calcsize('<L')

        while len(data) < payload_size:
            data += client_socket.recv(10485760)  # If you run into issues try 4096 bytes. 10mb = 10485760 bytes depending on your needs.

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack('<L', packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(10485760)  # If you run into issues try 4096 bytes. 10mb = 10485760 bytes depending on your needs.

        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Deserialize the received compressed frame
        compressed_frame = pickle.loads(frame_data)

        # Decompress the frame
        frame = cv2.imdecode(np.frombuffer(compressed_frame, dtype=np.uint8), -1)

        # Calculate and display the FPS and resolution
        frame_counter += 1

        if frame_counter >= 30:  # Calculate FPS every 30 frames
            end_time = time.time()
            elapsed_time = end_time - start_time  # Change this to actual elapsed time in seconds
            fps = frame_counter / elapsed_time
            resolution = f"FPS: {fps:.2f}, Resolution: {frame.shape[1]}x{frame.shape[0]}"
            print(resolution)
            frame_counter = 0
            start_time = time.time()  # Reset the start time for the next FPS calculation

        # Display the received frame with FPS and resolution
        cv2.putText(frame, resolution, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Drone Stream", frame)
        cv2.waitKey(1)  # Adjust the delay (e.g., 1ms) for smoother display

except KeyboardInterrupt:
    print("Server interrupted by user.")

except ConnectionResetError:
    print("Drone video feed has been disconnected.")
    disconnected = True

finally:
    # Clean up and release the socket
    server_socket.close()
    cv2.destroyAllWindows()

# Keep listening for a new connection if the previous one was disconnected
if disconnected:
    print("Waiting for a new drone feed connection...")


