import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
if cap.isOpened() == True:
    print("Acces Camera successfully!")
else: 
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Không thể lấy dc frame từ cap!")
        break
    cv2.imshow("image for cv2", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
print("Exit!")
cap.release()
cv2.destroyAllWindows()
    