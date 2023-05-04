import cv2


cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("camera has problem")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        print("camera did not read image")
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lists = cascade.detectMultiScale(frame_gray, minSize=(50, 50))

    for (x,y,w,h) in lists:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), thickness=2)
        # cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), thickness=-1)

    resized_img = cv2.resize(frame,(900, 900))

    cv2.imwrite('./room.jpg', resized_img)
    cv2.imshow('video image', resized_img)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
