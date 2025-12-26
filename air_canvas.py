import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks import python


# Initialize camera
cap = cv2.VideoCapture(0)

# Load Mediapipe HandLandmarker
base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)
detector = vision.HandLandmarker.create_from_options(options)

# Canvas
canvas = None
prev_x, prev_y = 0, 0

# Colors (BGR)
colors = [
    (255, 0, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 0, 0)
]
color_names = ["PURPLE", "BLUE", "GREEN", "YELLOW", "ERASER"]
current_color = colors[0]

def fingers_up(landmarks):
    # index finger tip vs PIP
    iy = landmarks[8].y
    iy_p = landmarks[6].y
    index_up = iy < iy_p

    my = landmarks[12].y
    my_p = landmarks[10].y
    middle_up = my < my_p

    return index_up, middle_up

def draw_palette(img):
    h, w, _ = img.shape
    box_w = w // len(colors)
    for i, col in enumerate(colors):
        x1 = i * box_w
        x2 = (i + 1) * box_w
        cv2.rectangle(img, (x1, 0), (x2, 60), col, -1)
        cv2.putText(img, color_names[i], (x1 + 10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)


while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    if canvas is None:
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

    draw_palette(frame)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    result = detector.detect(mp_image)

    mode = "NONE"

    if result.hand_landmarks:
        hand = result.hand_landmarks[0]  # first hand

        index_up, middle_up = fingers_up(hand)

        x = int(hand[8].x * w)
        y = int(hand[8].y * h)

        # selection
        if index_up and middle_up:
            mode = "SELECT"
            prev_x, prev_y = 0, 0

            if y < 60:
                box_w = w // len(colors)
                idx = x // box_w
                if idx < len(colors):
                    current_color = colors[idx]

            cv2.circle(frame, (x, y), 15, current_color, cv2.FILLED)

        # drawing
        elif index_up and not middle_up:
            mode = "DRAW"
            cv2.circle(frame, (x, y), 10, current_color, cv2.FILLED)

            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y

            thickness = 40 if current_color == (0, 0, 0) else 8
            cv2.line(canvas, (prev_x, prev_y), (x, y),
                     current_color, thickness)
            prev_x, prev_y = x, y

        else:
            prev_x, prev_y = 0, 0

    else:
        prev_x, prev_y = 0, 0

    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    cv2.putText(frame, f"Mode: {mode}",
                (10, h - 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 255), 2)

    cv2.putText(frame,
                "Index: Draw | Index+Middle: Color Select | C: Clear | Q: Quit",
                (10, h - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (255, 255, 255), 2)

    cv2.imshow("Air Canvas", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        canvas = np.zeros((h, w, 3), dtype=np.uint8)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

