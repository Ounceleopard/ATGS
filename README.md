# ATGS
Air To Ground Scanner. Software to deploy on a drone for tracking targets using FLIR.

 - Difference to the onboard software is that like a F-35 system you can connect different drone feeds to map out a field using machine learning. Smaller and faster drones can get closer to a target while flying on autopilot with commands from the homebase. This is to allow a command like receiver to have more situational awareness continuously. Meanwhile the tracking fleet can serve as overwatch and track human targets with FLIR at night and day.

 - Mapping out targets using python ai for unmanned drone fleets. Really the goal here is to make a open source program and make it free to use, a poor man's version of DJI flighthub 2. Not only looking at cost but also make it available to use on none industrial drones like Mavic 3 or the mini series. 

## Hardware 
- Drone: DJI Matrice 300 RTK Commercial Drone System

- FLIR Vue TZ20-R
https://advexure.com/products/flir-vue-tz20-dual-thermal-camera?variant=35654698467483

## Here's how this system works:

["ATGS"](https://github.com/Ounceleopard/ATGS/blob/5e9358e8b72b26d1699d89fa9c9483cab0a7f317/ATGS.py) Launches a friendly user interface to control the server and drone. <img width="712" alt="Screenshot 2023-09-28 at 1 07 24 AM" src="https://github.com/Ounceleopard/ATGS/assets/40043757/6f58f45e-f7a2-4c4a-aa6b-ff9400af4955">

["Drone"](https://github.com/Ounceleopard/ATGS/blob/460561252c650e820b6e57865ba6da00be8753f5/Drone.py) The drone feed pre-processes the captured video then sends it to the server. Using cv2 stream the video from the drone to the server and ultralytics Yolov8 for detection and annotation models. 

["Server"](https://github.com/Ounceleopard/ATGS/blob/e4a9ffe2593d767fd62e7d9838dc2c58d8656a08/Server.py) This is the homebase to where different drones stream their video feed. Here is where the video window clients are launched. 

### Install

```bash
# Create python virtual environment
python3 -m venv venv

# Install dependencies
pip install -r requirements.txt

# Sometimes lap install doesn't work
pip install lapx
```
### Execute

```bash
# launch 
python3 ATGS.py
```
### Current State

- Operational
<img width="947" alt="Screenshot 2023-09-26 at 11 28 41 AM" src="https://github.com/Ounceleopard/ATGS/assets/40043757/9959ed31-502b-43b7-987f-da75c8ececc2">


### Disclaimer
This code for educational purposes only, do not attempt. I am not liable for any damages or injuries.
