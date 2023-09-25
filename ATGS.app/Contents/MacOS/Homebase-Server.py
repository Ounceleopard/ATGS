import cv2
import numpy as np
from flask import Flask, request, Response

app = Flask(__name__)

# Initialize video capture for the homebase server
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

def generate():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Encode the frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/upload', methods=['POST'])
def upload():
    # Receive frames from the remote camera and display them
    frame = request.data
    nparr = np.frombuffer(frame, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow("Homebase Server", img)
    cv2.waitKey(1)  # Display the frame

    return "Frame received successfully."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Change host and port as needed


# Video to recon network 

import cv2
import numpy as np
import requests
import time
import pyrtmp

# Set the RTMP server address and stream key
rtmp_server = "rtmp://your_rtmp_server_ip/live"
stream_key = "your_stream_key"

# Initialize video capture for the homebase server
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

# Initialize the RTMP client
client = pyrtmp.Client(rtmp_server)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Encode the frame as JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    frame_bytes = buffer.tobytes()

    try:
        # Send the frame to the RTMP server
        client.write(frame_bytes)
    except pyrtmp.RtmpException as e:
        print(f"Error sending frame to RTMP server: {e}")
        time.sleep(1)  # Retry after a delay in case of an error

cap.release()


"""
To send the video feed from the homebase server to multiple video receiving servers, you can use a broadcasting or streaming protocol. One common choice is to use the Real-Time Messaging Protocol (RTMP) for this purpose. 
You'll need to set up a video streaming server that supports RTMP, such as Nginx with the RTMP module or a dedicated media server like Wowza. Here's a high-level overview of how this can be accomplished:

1. Set Up RTMP Server: Install and configure an RTMP server on your homebase server or another dedicated server. For example, you can use Nginx with the RTMP module. Follow the documentation of your chosen server to set it up properly.

2. Modify Homebase Server (Sender): Modify the homebase server code to stream video to the RTMP server using the RTMP protocol. You can use a Python library like `pyrtmp` to accomplish this. Here's an example of how you can modify the homebase server code:

3. Set Up Video Receiving Servers (Clients): On the receiving end, set up one or more video receiving servers (clients) that can connect to the RTMP server to receive and display the video feed. These can be other servers or devices running software that 
can play RTMP streams, such as VLC, FFmpeg, or a web-based player.

The homebase server will send the video feed to the RTMP server, and the receiving servers will connect to the RTMP server to receive and display the live stream. Be sure to configure the receiving servers with the appropriate RTMP stream URL, 
which includes the server address and stream key you specified in step 1.

Please note that setting up an RTMP server and configuring the receiving servers can be complex, and the specifics may vary depending on your chosen software. Make sure to consult the documentation of your selected RTMP server and clients for detailed setup instructions.
"""
