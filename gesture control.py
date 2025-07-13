import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe hand detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Start webcam
cap = cv2.VideoCapture(0)

def fingers_status(hand_landmarks):
    """Return which fingers are up"""
    landmarks = hand_landmarks.landmark

    status = {
        'thumb': landmarks[4].x > landmarks[3].x,
        'index': landmarks[8].y < landmarks[6].y,
        'middle': landmarks[12].y < landmarks[10].y,
        'ring': landmarks[16].y < landmarks[14].y,
        'pinky': landmarks[20].y < landmarks[18].y
    }
    return status

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            status = fingers_status(hand_landmarks)

            # Gesture detection
            if status['index'] and not status['middle'] and not status['ring'] and not status['pinky']:
                pyautogui.press('up')
                cv2.putText(frame, "UP", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            elif not any(status.values()):
                pyautogui.press('down')
                cv2.putText(frame, "DOWN", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            elif status['index'] and status['middle'] and not status['ring'] and not status['pinky']:
                pyautogui.press('left')
                cv2.putText(frame, "LEFT", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            elif status['index'] and status['middle'] and status['ring'] and status['pinky']:
                pyautogui.press('right')
                cv2.putText(frame, "RIGHT", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Optional: Show how many fingers are up
            count = sum(status.values())
            cv2.putText(frame, f"Fingers: {count}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)

    cv2.imshow("Hand Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
