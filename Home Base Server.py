import cv2
import socket
import pickle
import struct

# Set the server IP address and port to listen on
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)  # Listen for up to 5 client connections

print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

# Accept a client connection
client_socket, addr = server_socket.accept()
print(f"Connection established with {addr}")

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
    #if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
    
    cv2.imshow("Received Video", frame)
    cv2.waitKey(1)

# Close the server and client sockets
client_socket.close()
server_socket.close()
cv2.destroyAllWindows()
