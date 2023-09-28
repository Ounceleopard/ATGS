# ATGS
Air To Ground Scanner. Software to deploy on a drone for tracking targets using FLIR.

 - Difference to the onboard software is that like a F-35 system you can connect different drone feeds to map out a field using machine learning. Smaller and faster drones can get closer to a target while flying on autopilot with commands from the homebase. This is to allow a command like receiver to have more situational awareness continuously. Meanwhile the tracking fleet can serve as overwatch and track human targets with FLIR at night and day.

 - Mapping out targets using python ai for unmanned drone fleets. Really the goal here is to make a open source program and make it free to use, a poor man's version of DJI flighthub 2. Not only looking at cost but also make it available to use on none industrial drones like Mavic 3 or the mini series. 

## Hardware 
- Drone: DJI Matrice 300 RTK Commercial Drone System

- FLIR Vue TZ20-R
https://advexure.com/products/flir-vue-tz20-dual-thermal-camera?variant=35654698467483

- DJI Zenmuse L1 LiDAR + RGB Survey Camera
https://advexure.com/products/dji-zenmuse-l1-lidar-rgb-survey-camera?variant=40651659280539&gclid=Cj0KCQjw9rSoBhCiARIsAFOiplmTn5G7HRZmRkekjJT0IEAaU19JAP3UyloXs37CFivfynbKI8rzf08aAoBWEALw_wcB

## Here's how this system works:

["ATGS"](https://github.com/Ounceleopard/ATGS/blob/e4a9ffe2593d767fd62e7d9838dc2c58d8656a08/ATGS.py) Launches a friendly user interface to control the server and drone.
<img width="712" alt="Screenshot 2023-09-28 at 1 07 24 AM" src="https://github.com/Ounceleopard/ATGS/assets/40043757/b5da455a-5bb8-4399-84f3-a1974c444003">

["Drone"](https://github.com/Ounceleopard/ATGS/blob/460561252c650e820b6e57865ba6da00be8753f5/Drone.py) The drone feed pre-processes the captured video then sends it to the server. Using cv2 stream the video from the drone to the server and ultralytics Yolov8 for detection and annotation models. 

["Server"](https://github.com/Ounceleopard/ATGS/blob/e4a9ffe2593d767fd62e7d9838dc2c58d8656a08/Server.py) This is the homebase to where different drones stream their video feed. Here is where the video window clients are launched. 

### Install

```bash
# Create python virtual environment
python -m venv venv

# Install dependencies
pip install -r requirements.txt
```

### Execute

```bash
# Sometimes lap install doesn't work
pip install lapx

# launch 
python3 ATGS.py
```

### Example 
- Code needs improvement but heres where I think I can get it in a few months.
  
![park-people-smart-city-computer-vision-use-case-visoai-e1660257558388-1536x1340](https://github.com/Ounceleopard/F-35-ATGS/assets/40043757/a378ccec-b183-443b-b4df-e7013ec92b28)

### Current State
- Patch 2 EST: OCT 10th 2023

<img width="947" alt="Screenshot 2023-09-26 at 11 28 41 AM" src="https://github.com/Ounceleopard/ATGS/assets/40043757/ddddbfd7-4ab3-40df-9af8-a6708de8f50c">

### Disclaimer
This code for educational purposes only, do not attempt. I am not liable for any damages or injuries.
