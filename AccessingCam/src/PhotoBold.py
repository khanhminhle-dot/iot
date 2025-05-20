import cv2
import datetime
from gpiozero import Button

# Setup GPIO buttons (GPIO.BCM)
button1 = Button(17)  # Kính
button2 = Button(18)  # Mũ
button3 = Button(27)  # Râu
button4 = Button(22)  # Lưu ảnh

# Khởi động camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Không thể mở camera")
    exit()

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_mcs_nose.xml")

# Load ảnh phụ kiện PNG có alpha
glass_imgs = [cv2.imread(f"glasses/glasses/{i}.png", cv2.IMREAD_UNCHANGED) for i in range(1, 6)]
hat_imgs = [cv2.imread(f"hats/hats/{i}.png", cv2.IMREAD_UNCHANGED) for i in range(1, 5)]
mustache_imgs = [cv2.imread(f"mustaches/mustaches/{i}.png", cv2.IMREAD_UNCHANGED) for i in range(1, 7)]

glass_idx, hat_idx, mustache_idx = 0, 0, 0
last_frame = None  # để lưu khi nhấn nút

def overlay_transparent(bg, overlay, x, y, target_width, target_height):
    if overlay is None:
        return bg

    overlay_resized = cv2.resize(overlay, (target_width, target_height))
    h, w = overlay_resized.shape[:2]

    if x < 0 or y < 0 or x + w > bg.shape[1] or y + h > bg.shape[0]:
        return bg

    overlay_img = overlay_resized[:, :, :3]
    mask = overlay_resized[:, :, 3] / 255.0
    mask = cv2.merge([mask, mask, mask])

    roi = bg[y:y+h, x:x+w]
    bg[y:y+h, x:x+w] = (1 - mask) * roi + mask * overlay_img
    return bg

# ======== Các hàm xử lý nút bấm =========
def change_glass():
    global glass_idx
    glass_idx += 1
    print(">> Chuyển kính:", glass_idx % len(glass_imgs))

def change_hat():
    global hat_idx
    hat_idx += 1
    print(">> Chuyển mũ:", hat_idx % len(hat_imgs))

def change_mustache():
    global mustache_idx
    mustache_idx += 1
    print(">> Chuyển râu:", mustache_idx % len(mustache_imgs))

def save_image():
    global last_frame
    if last_frame is not None:
        filename = f"snapshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, last_frame)
        print(">> Ảnh đã lưu:", filename)

# Gán chức năng cho từng nút
button1.when_pressed = change_glass
button2.when_pressed = change_hat
button3.when_pressed = change_mustache
button4.when_pressed = save_image

# ======== Vòng lặp chính =========
while True:
    ret, frame = cap.read()
    if not ret:
        print("Không thể đọc camera")
        break

    last_frame = frame.copy()  # lưu frame để dùng khi cần lưu ảnh
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]

        # Mũ
        hat = hat_imgs[hat_idx % len(hat_imgs)]
        frame = overlay_transparent(frame, hat, x, y - int(h * 0.6), w, int(h * 0.6))

        # Kính
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        for (ex, ey, ew, eh) in eyes[:1]:
            glass = glass_imgs[glass_idx % len(glass_imgs)]
            frame = overlay_transparent(frame, glass, x + ex - 5, y + ey, ew + 10, int(eh * 1.5))

        # Râu
        noses = nose_cascade.detectMultiScale(roi_gray, 1.1, 5)
        for (nx, ny, nw, nh) in noses[:1]:
            mustache = mustache_imgs[mustache_idx % len(mustache_imgs)]
            frame = overlay_transparent(frame, mustache, x + nx, y + ny + nh//2, nw, int(nh * 0.7))

    cv2.imshow("Fun Face with GPIO Buttons", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
