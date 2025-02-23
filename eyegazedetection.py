import cv2
import dlib
import numpy as np

# Load pre-trained model for landmark detection
detector = dlib.get_frontal_face_detector()  #through reearch i found this pre built facial landmark model and downloaded it in the system
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def calculate_gaze_direction(eye_points):
#calculating the center of the eye 
    left_eye_center = np.mean(eye_points[0], axis=0)
    right_eye_center = np.mean(eye_points[1], axis=0)
    
#determinig the direction of eyes
    gaze_direction = right_eye_center - left_eye_center
    
    return gaze_direction

def is_looking_at_screen(gaze_direction):
    # at this point it checks whether the person is still looking at the screen
    threshold = 0.4  # the threshold value is to determine at which value warning should be given, the lower the value higher the chances of warning
    return np.linalg.norm(gaze_direction) < threshold

def issue_warning():
    print("Warning: keep your focus at the screen!")

def detect_gaze(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)
        
        # Extracts eye landmarks left and right eyes for the direction of gazes
        left_eye_points = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(36, 42)])
        right_eye_points = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(42, 48)])
        
        # determines the direction of eyegazes  
        gaze_direction = calculate_gaze_direction((left_eye_points, right_eye_points))
        
    # Checks if gaze is on screen
        if not is_looking_at_screen(gaze_direction):
            issue_warning()

# Draws rectangles around eyes for visualization
        cv2.polylines(frame, [left_eye_points], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.polylines(frame, [right_eye_points], isClosed=True, color=(0, 255, 0), thickness=2)

# Video capture is initialized 
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detect_gaze(frame)
    
    cv2.imshow('Eye Gaze Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
