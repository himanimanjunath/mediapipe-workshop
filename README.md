# Mediapipe Workshop
Using OpenCV and MediaPipe to do real-time pose detection using your webcam.

## Features + How it Works 
* Detects 33 body landmarks (shoulders, knees, etc) using MediaPipe's Pose model 
* Draws joint connections (landmarks) and labels them in real time using OpenCV
* Tracks the confidence of each landmark
* Real-time performance using webcam
* Exit by pressing `esc`

## Main Libraries Used
* cv2 – OpenCV, used for camera input and image processing
* mediapipe – Google's machine learning library for face/pose/hand tracking

## Process
1. Import libraries
2. Initialize drawing and pose detection tools
3. Open webcam (camera index 1, which might be an external webcam)
4. Run a loop while the camera is active
5. Read and process each frame:
   - Flip horizontally so it behaves like a mirror
   - Convert BGR (OpenCV format) to RGB (MediaPipe format)
   - Run pose estimation
   - Convert back to BGR for OpenCV display
6. Draw landmarks like joints/body points if pose is detected:
   - Overlay body connections
   - Print index and confidence at each joint using `cv2.putText`
7. Show image in new window 
8. Exit the loop by pressing `esc`

## Output
Live webcam feed with detected body joints and their confidence values drawn on top.

## Try it out!

### Requirements
* Python 3.7+
* OpenCV
* MediaPipe

### Installation
```bash
python pose_detect.py
```

### Run the program
```bash
pip install opencv-python mediapipe
```
If your webcam doesn't turn on, try changing the camera index in cv2.VideoCapture(1) to 0.

### Exit
Press `esc` to close the webcam window and stop the program.

