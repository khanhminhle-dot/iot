import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened(): 
    print("Access camera fail!")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_eye.xml")
nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_mcs_nose.xml")

while True:
    ret, frame = cap.read()
    if not ret :
        print("k the lay anh")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    print("Số khuôn mặt phát hiện: ", len(faces))
    for (x, y, w , h) in faces:
        cv2.rectangle(frame, (x, y), (x+w , y+h), (0, 255, 0), 2)
    # end
    cv2.imshow("face, nose, eye ", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("successfully")
