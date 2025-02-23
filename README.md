
# Eye Gaze Detection Project

## Overview

This project implements an eye gaze detection system using Python, OpenCV, and Dlib. The system tracks the user's eye gaze in real-time through a webcam and issues a warning if the gaze is not directed at the screen. This application can be useful in scenarios such as online examinations, presentations, or any situation where maintaining focus on the screen is essential.

## Features

- Real-time eye gaze detection using webcam input.
- Visual feedback with highlighted eyes in the video feed.
- Warning system that alerts users when they look away from the screen.
- Simple and easy to use.

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.x
- OpenCV
- Dlib
- Numpy
- Imutils (optional for image processing)

You can install the required libraries using pip:

```bash
pip install opencv-python dlib numpy imutils
```

### Download Dlib's Model

You need to download Dlib's facial landmark predictor model:

1. Download the model from [Dlib's model repository](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2).
2. Extract the `.bz2` file to get `shape_predictor_68_face_landmarks.dat`.
3. Place the `.dat` file in the same directory as your project.

## Usage

1. Clone this repository or download the project files.
2. Open a terminal and navigate to the project directory.
3. Run the script:

   ```bash
   python eye_gaze_detection.py
   ```

4. Ensure your webcam is connected and functional.
5. Position yourself in front of the camera, and the system will start detecting your eye gaze immediately.

### Stopping the Program

To stop the program, simply press `q` while the output window is active.

## Code Explanation

- **Video Capture**: The code captures video frames from your webcam.
- **Face Detection**: Dlib's frontal face detector identifies faces in each frame.
- **Landmark Detection**: The code extracts eye landmarks to calculate gaze direction.
- **Gaze Checking**: It checks if the user's gaze is directed at the screen based on a defined threshold.
- **Warning System**: If the user looks away from the screen, a warning message is printed to the console.

## Customization

You can adjust various parameters in the code:

- **Threshold Value**: Modify the threshold value in `is_looking_at_screen` function to change sensitivity for gaze detection.
  
  ```python
  threshold = 0.4  # Adjust this value based on your requirements
  ```

## Troubleshooting

If you encounter issues:

- Ensure that your webcam is properly connected and accessible by OpenCV.
- Check that all required libraries are installed correctly.
- Make sure that `shape_predictor_68_face_landmarks.dat` is located in the project directory.

## License

This project is open-source and available under the MIT License.

