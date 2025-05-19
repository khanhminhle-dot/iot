import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print("lôi k thể lấy ảnh")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 5)
    
    print("Số khuôn mặt phát hiện:", len(faces))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow("image", frame)
    key = cv2.waitKey(1) & 0xff
    if key == ord('q') :
        break
cap.release()
cv2.destroyAllWindows()

'''
   face_cascade = cv2.CascadeClasifier(cv2.data.haarcascade+"haarcascade_frontialface_default.xml")
   face = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
   len_Face = len(face)
'''