import cv2
import mediapipe as mp
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

print("Step 1: All libraries loaded.")

# Webcam setup
cap = cv2.VideoCapture(0)
print("Step 2: Webcam initialized.")

# MediaPipe hands setup
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
print("Step 3: MediaPipe hand tracker ready.")

# Audio setup using Pycaw
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]
print(f"Step 4: Volume range is {min_vol} dB to {max_vol} dB")

# Main loop
while True:
    success, img = cap.read()
    if not success:
        print("Webcam frame not captured.")
        continue

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        print("Step 6: Hand detected.")
        handLms = results.multi_hand_landmarks[0]
        lmList = []

        for id, lm in enumerate(handLms.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append((id, cx, cy))

        if lmList:
            print("Step 7: Landmarks collected.")
            x1, y1 = lmList[4][1], lmList[4][2]   # Thumb tip
            x2, y2 = lmList[8][1], lmList[8][2]   # Index tip

            length = math.hypot(x2 - x1, y2 - y1)
            print(f"Step 8: Distance between fingers: {length:.2f}")

            # Convert distance to volume level
            vol = np.interp(length, [30, 200], [min_vol, max_vol])
            volume.SetMasterVolumeLevel(vol, None)
            print(f"Step 9: Volume set to {vol:.2f} dB")

            # Draw gesture indicators
            cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

            # Draw volume bar
            vol_bar = np.interp(length, [30, 200], [400, 150])
            cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
            cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv2.FILLED)

            # Show volume percentage
            cv2.putText(img, f'{int(np.interp(length, [30, 200], [0, 100]))} %',
                        (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    else:
        print("No hand detected.")

    cv2.imshow("Gesture Volume Control", img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting program...")
        break

cap.release()
cv2.destroyAllWindows()
print("Webcam and windows closed cleanly.")


