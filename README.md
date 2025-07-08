# Gesture-Based Volume Controller using MediaPipe and OpenCV

This project leverages **computer vision** to control system volume using hand gestures captured via a webcam. It utilizes **MediaPipe** for hand landmark detection and **OpenCV** for real-time video processing. By tracking the distance between the thumb and index finger, the system dynamically adjusts the audio volume.

## Features

- Real-time hand gesture detection using webcam
- Volume control by adjusting finger distance
- Visual feedback with gesture drawing and volume bar
- Smooth integration with system audio using Pycaw
- No physical contact needed – fully gesture-controlled

## Technologies Used

- Python
- MediaPipe (for hand tracking)
- OpenCV (for video and image processing)
- Pycaw (for controlling Windows system volume)
- NumPy, Math

## How It Works

1. Capture webcam feed using OpenCV
2. Detect hand landmarks with MediaPipe
3. Measure distance between thumb and index finger
4. Convert that distance to a volume level
5. Use Pycaw to set the system volume in real-time
6. Display visual indicators and feedback on screen

## Requirements

- Python 3.10 (MediaPipe doesn't support 3.13+)
- Webcam (built-in or external)
- Windows OS (Pycaw is Windows-specific)

## How to Run

1. Clone or download this repository.
2. Create and activate a Python 3.10 virtual environment:
3. Install the dependencies
4. Run the script
5. Show your hand to the webcam and adjust the volume with your fingers.

5. Show your hand to the webcam and adjust the volume with your fingers.

## Output

- Displays live video with detected hand landmarks
- Shows a volume bar and percentage on screen
- Adjusts your system volume smoothly as you pinch or spread fingers

## Results

- Successfully controls system volume based on hand gestures
- Fast and accurate hand tracking using MediaPipe
- Real-time responsiveness with minimal lag
- Effective visual feedback for user interaction
- Eliminates need for hardware buttons, enabling touchless control

> This project demonstrates an innovative, touch-free approach to human-computer interaction using gesture control.
