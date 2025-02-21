import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(1)

#loop that keeps your camera running till you turn it off
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
   #while loop continuosuly till the camera is opened
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame")
            continue

        image = cv2.cvtColor(cv2.flip(image,1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
            h,w,z = image.shape

            for idx, landmark in enumerate(results.pose_landmarks.landmark):
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                confidence = landmark.visibility
                cv2.putText(image, f"{idx} ({confidence:.2f})", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2, cv2.LINE_AA)

        #function to open the display of a camera 
        cv2.imshow("Mediapipe pose", image)

        #if ESC key is pressed, exits the camera 
        if cv2.waitKey(5) & 0xFF ==27:
            break

cap.release()
cv2.destroyAllWindows()
        

