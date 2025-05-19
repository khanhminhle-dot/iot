import cv2
from pathlib import Path
cap = cv2.VideoCapture(0)
if not cap.isOpened(): 
    print("Access camera fail!")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 440)

output_folder = Path(__file__).resolve().parent / "images"
output_folder.mkdir(exist_ok=True)
n = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can not access frame from camera!")
        break

    cv2.imshow("My Image", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        filename  = output_folder / f"image_capture_{n}.jpg"
        cv2.imwrite(str(filename), frame)
        print(f"Captured image_capture_{n}.jpg")
        n += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
