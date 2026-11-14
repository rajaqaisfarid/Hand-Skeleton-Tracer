import cv2
import mediapipe as mp
import numpy as np
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7,
    max_num_hands=2
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

skeleton_mode = False
snap_cooldown = 0

while True:
    success, img = cap.read()
    if not success:
        break
        
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    black_canvas = np.zeros((h, w, c), dtype=np.uint8)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            
            thumb_tip = hand_landmarks.landmark[4]
            middle_tip = hand_landmarks.landmark[12]

            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)
            mx, my = int(middle_tip.x * w), int(middle_tip.y * h)

            distance = math.hypot(mx - tx, my - ty)
            
            if distance < 35 and snap_cooldown == 0:
                skeleton_mode = not skeleton_mode
                snap_cooldown = 20 # Freeze toggle for 20 frames so it doesn't flicker
            
            if skeleton_mode:
                mp_draw.draw_landmarks(black_canvas, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            else:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
    if snap_cooldown > 0:
        snap_cooldown -= 1
        
    display_img = black_canvas if skeleton_mode else img
    
    cv2.imshow("Hand Tracking - Snap to Toggle", display_img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()