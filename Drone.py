# Drone

import cv2
import socket
import pickle
import struct
from ultralytics import YOLO
import supervision as sv

#######################
# Define the IP address and port of the homebase server
homebase_ip = '127.0.0.1'  # Change this to the actual IP address
homebase_port = 8080       # Change this to the actual Port address 
DroneVideoSource = 0       # (You may need to change this based on your camera source)
########################

# Define video settings for the drone
drone_video_width = 1280  # Set the desired width (e.g., 320 for lower resolution)
drone_video_height = 720  # Set the desired height (e.g., 240 for lower resolution)
drone_video_fps = 30  # Set the desired frame rate (e.g., 30 fps)

# Define a line zone for counting objects
LINE_START = sv.Point(600, 900)
LINE_END = sv.Point(600, 100)

def main():
    # Initialize the line counter and annotators
    line_counter = sv.LineZone(start=LINE_START, end=LINE_END)
    line_annotator = sv.LineZoneAnnotator(thickness=2, text_thickness=1, text_scale=0.5)
    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=1,
        text_scale=0.5
    )

    # Choose the YOLO model size (options ranging from small to big)
    model = YOLO("yolov8n.pt")  # You can choose a different model size here
    #model = YOLO("yolov8s.pt")
    #model = YOLO("yolov8m.pt")
    #model = YOLO("yolov8l.pt")
    #model = YOLO("yolov8x.pt")

    # Create a VideoCapture object with custom resolution and fps
    cap = cv2.VideoCapture(DroneVideoSource)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, drone_video_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, drone_video_height)
    cap.set(cv2.CAP_PROP_FPS, drone_video_fps)

    # Create a socket to send frames and detections to the homebase server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((homebase_ip, homebase_port))
        print("Connection to homebase server established.")
                                                        
        for result in model.track(source=DroneVideoSource, show=False, stream=True, agnostic_nms=True):
            frame = result.orig_img
            detections = sv.Detections.from_yolov8(result)

            if result.boxes.id is not None:
                detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)

            # Filter out specific class IDs (e.g., class_id 60 and 0)
            detections = detections[(detections.class_id != 60) & (detections.class_id != 0)]

            # Generate labels for the detected objects
            labels = [
                f"{tracker_id} {model.model.names[class_id]} {confidence:0.10f}"
                for _, confidence, class_id, tracker_id
                in detections
            ]

            # Annotate the frame with bounding boxes and labels
            frame = box_annotator.annotate(
                scene=frame,
                detections=detections,
                labels=labels
            )

            # Update the line counter and annotate the frame with counting information
            line_counter.trigger(detections=detections)
            line_annotator.annotate(frame=frame, line_counter=line_counter)

            # Compress the frame as JPEG
            _, compressed_frame = cv2.imencode('.jpg', frame)
            
            # Serialize the compressed frame and send it to the homebase server
            frame_data = pickle.dumps(compressed_frame)
            client_socket.sendall(struct.pack('<L', len(frame_data)) + frame_data)

            # Exit the loop when the 'Esc' key is pressed (ASCII code 27)
            if (cv2.waitKey(30) == 27):
                break

    except ConnectionRefusedError:
        print("Failed to connect to homebase server. Make sure the server is running.")
    finally:
        # Release the video capture, close OpenCV windows, and close the socket
        cap.release()
        cv2.destroyAllWindows()
        client_socket.close()

if __name__ == "__main__":
    main()

