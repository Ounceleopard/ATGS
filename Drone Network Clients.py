import cv2
import socket
import pickle
import struct

# Set the IP address and port to receive data from the sender
# http://127.0.0.1:8080/
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

# Create a socket to receive data
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the sender
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print(f"Connected to {SERVER_IP}:{SERVER_PORT}")

    # Create a window to display the received video
    cv2.namedWindow("Received Video", cv2.WINDOW_NORMAL)

    data = b""
    payload_size = struct.calcsize('Q')

    while True:
        # Receive the size of the incoming data
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # Adjust buffer size if needed
            if not packet:
                break
            data += packet

        # Extract the frame size and data
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        # Receive the frame data
        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)  # Adjust buffer size if needed
        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Deserialize the frame
        frame = pickle.loads(frame_data)

        # Display the received frame
        cv2.imshow("Received Video", frame)
        cv2.waitKey(1)

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    client_socket.close()
    cv2.destroyAllWindows()
