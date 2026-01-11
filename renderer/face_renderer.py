import cv2
import numpy as np

def render_face(motion, fps=30):
    frames = []
    h, w = 512, 512

    for i in range(len(motion["mouth_open"])):
        img = np.ones((h, w, 3), dtype=np.uint8) * 255

        cx = w // 2 + int(motion["head_sway"][i])
        cy = h // 2 + int(motion["head_nod"][i])

        # Head
        cv2.circle(img, (cx, cy), 150, (0, 0, 0), 3)

        # Eyes
        eye_open = 1 - motion["blink"][i]
        eye_h = int(10 * eye_open)

        cv2.ellipse(img, (cx - 50, cy - 40), (12, eye_h), 0, 0, 360, (0,0,0), -1)
        cv2.ellipse(img, (cx + 50, cy - 40), (12, eye_h), 0, 0, 360, (0,0,0), -1)

        # Mouth
        mouth_h = int(10 + motion["jaw_drop"][i] * 40)
        mouth_w = int(30 + motion["lip_width"][i] * 30)

        cv2.ellipse(
            img,
            (cx, cy + 60),
            (mouth_w, mouth_h),
            0, 0, 180,
            (0,0,0),
            3
        )

        frames.append(img)

    return frames
