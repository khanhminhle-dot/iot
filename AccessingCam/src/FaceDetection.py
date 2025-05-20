import cv2
from gpiozero import LED
from time import sleep

# Khởi tạo 5 đèn LED tương ứng với 5 người
led_pins = [5, 6, 13, 19, 26]  # GPIO BCM
leds = [LED(pin) for pin in led_pins]

# Hàm bật đúng số lượng đèn
def update_leds(face_count):
    for i in range(len(leds)):
        if i < face_count:
            leds[i].on()
        else:
            leds[i].off()

# Khởi tạo cascade và camera
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Lỗi: không thể lấy ảnh")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    face_count = min(len(faces), 5)  # giới hạn tối đa 5 người
    print("Số khuôn mặt phát hiện:", len(faces))
    update_leds(face_count)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("image", frame)
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        break

# Tắt đèn & camera
for led in leds:
    led.off()
cap.release()
cv2.destroyAllWindows()


'''
   face_cascade = cv2.CascadeClasifier(cv2.data.haarcascade+"haarcascade_frontialface_default.xml")
   face = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
   len_Face = len(face)
'''