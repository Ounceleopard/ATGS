# Server: Takes and displays the feed from the drone
import cv2
import socket
import pickle
import struct
import numpy as np

# Define the server IP address and port
server_ip = '127.0.0.1'  # Change this to your desired IP address
server_port = 8080  # Change this to your desired port number

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5) # 5 Different clients can connect.

print("Server is listening for incoming connections...")

try:
    client_socket, addr = server_socket.accept()
    print(f"Drone feed connection established from {addr}.")
    disconnected = False

    # Create a window for displaying the video feed
    #cv2.namedWindow("Drone Feed", cv2.WINDOW_NORMAL)

    while True:
        data = b''
        payload_size = struct.calcsize('<L')

        while len(data) < payload_size:
            data += client_socket.recv(4096)

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack('<L', packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Deserialize the received compressed frame
        compressed_frame = pickle.loads(frame_data)

        # Decompress the frame
        frame = cv2.imdecode(np.frombuffer(compressed_frame, dtype=np.uint8), -1)

        # Output confirmation to terminal
        print("Received frame from drone.")

        # Display the received frame
        cv2.imshow("Drone Video Stream", frame)
        cv2.waitKey(10)  # Adjust the delay (e.g., 10ms) as needed for smoother display

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


