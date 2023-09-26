# ATGS
Air To Ground Scanner. Software to deploy on a drone for tracking targets using FLIR.

Difference to the onboard software is that like a F-35 you can connect different drone feeds to map out a field. 
Smaller and faster drones can get closer to a target while, the "recon" drone fleet can map out the situation. 
This is to allow a command like receiver or leader to have more situational awareness continuously.

Mapping out targets using python ai for unmanned drone fleets.

# Hardware 
(Not model specific required but if budget allows)

- Drone: DJI Matrice 300 RTK Commercial Drone System

- FLIR Vue TZ20-R
https://advexure.com/products/flir-vue-tz20-dual-thermal-camera?variant=35654698467483

or:

- DJI Zenmuse L1 LiDAR + RGB Survey Camera
https://advexure.com/products/dji-zenmuse-l1-lidar-rgb-survey-camera?variant=40651659280539&gclid=Cj0KCQjw9rSoBhCiARIsAFOiplmTn5G7HRZmRkekjJT0IEAaU19JAP3UyloXs37CFivfynbKI8rzf08aAoBWEALw_wcB

# Here's how this system works:

The ["Drone-Tracker-Feed"](https://github.com/Ounceleopard/ATGS/blob/0ca643cf28a121eebf4aa12d1f5da530d7ed83f4/Drone-Tracker-Feed.py) captures video frames from a drone (you can specify a different source if needed like your iphone) and tracking objects within those frames using the MIL (Multiple Instance Learning) tracking algorithm, and sending the video frames to a server over a network connection.

The ["Home-Base-Server"](https://github.com/Ounceleopard/ATGS/blob/0ca643cf28a121eebf4aa12d1f5da530d7ed83f4/Home-Base-Server.py) receives these frames, deserializes them, and displays them in a window using OpenCV (cv2).

The ["Drone-Network-Clients"](https://github.com/Ounceleopard/ATGS/blob/9db591fbfdaf603dee81ed5483d2f5cc526f737e/Drone-Network-Clients.py) is a program that connects to a server over a network, receives video frames sent by the server, deserializes these frames, and displays them in a window using OpenCV (cv2). Goal here is to involve more ai and have commends from the home base server to this program so that the drones can track without a human pilot.

# Example 
Code needs improvement but heres where I think I can get it in a few months.
![park-people-smart-city-computer-vision-use-case-visoai-e1660257558388-1536x1340](https://github.com/Ounceleopard/F-35-ATGS/assets/40043757/a378ccec-b183-443b-b4df-e7013ec92b28)
![video-analysis-background-substraction-opencv-knn-method-1536x576](https://github.com/Ounceleopard/F-35-ATGS/assets/40043757/af09fe03-450c-4452-82bc-c111d9d5c360)

# Disclaimer
This code for educational purposes only, do not attempt. I am not liable for any damages or injuries.
