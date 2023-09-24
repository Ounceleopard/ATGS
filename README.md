# F-35-ATGS
Air To Ground Scanner. Software to deploy on a drone for tracking targets using FLIR.

Difference to the onboard software is that like a F-35 you can connect different drone feeds to map out a field. 
Fast attack drones to provide a closer approach to target while, the recon drone fleet can map out the situation.

Mapping out targets using python ai for unmanned drone fleets.

# Hardware 
(Not model specific required but if budget allows)

Drone: DJI Matrice 300 RTK Commercial Drone System

FLIR Vue TZ20-R
https://advexure.com/products/flir-vue-tz20-dual-thermal-camera?variant=35654698467483

or: 

DJI Zenmuse L1 LiDAR + RGB Survey Camera
https://advexure.com/products/dji-zenmuse-l1-lidar-rgb-survey-camera?variant=40651659280539&gclid=Cj0KCQjw9rSoBhCiARIsAFOiplmTn5G7HRZmRkekjJT0IEAaU19JAP3UyloXs37CFivfynbKI8rzf08aAoBWEALw_wcB


Here's how this system works:

The "Remote Camera (Client)" captures video frames from a camera (you can specify a different source if needed) and sends them as JPEG frames to the homebase server via HTTP POST requests.

The "Homebase Server (Server)" uses Flask to create a server that listens for incoming frames from the remote camera. It receives the frames, decodes them, and displays them using OpenCV.

Make sure to replace "your_homebase_server_ip" and "your_homebase_server_port" with the actual IP address and port where your homebase server is running. Run the client code on the remote camera device, and run the server code on your homebase server. You can access the video feed by opening a web browser and navigating to http://<homebase_server_ip>:<port>.

# Example 
Code needs improvement but heres where I think I can get it in a few months.
![park-people-smart-city-computer-vision-use-case-visoai-e1660257558388-1536x1340](https://github.com/Ounceleopard/F-35-ATGS/assets/40043757/a378ccec-b183-443b-b4df-e7013ec92b28)
![video-analysis-background-substraction-opencv-knn-method-1536x576](https://github.com/Ounceleopard/F-35-ATGS/assets/40043757/af09fe03-450c-4452-82bc-c111d9d5c360)
