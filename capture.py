# """
import cv2
import datetime
import os
import subprocess


class camera_oneshot_class():
    def camera_oneshot(self):
        camera_id = 0
        deviceid=0 # it depends on the order of USB connection.
        delay = 1
        window_name = 'frame'

        try:
            os.chdir("./images")
        except:
            os.mkdir("./images")

        capture = cv2.VideoCapture(deviceid)


        num = 0
        time = datetime.datetime.now()
        # print(type(time))
        time = str(time)
        # print(type(time))
        # print(time)
        time = time.replace(" ", "_").replace("-", "_").replace(":", "_").replace(time[19:26], "")

        # print(time)
        file_name = str(time)

        dirname = "./images"

        cmd = "mv " + file_name + ".jpg " + dirname

        while(True):
            ret, frame = capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (0, 0), 5)

            cv2.imshow(window_name, frame)

            if cv2.waitKey(1) & 0xFF == ord('v'):       # video start

                cv2.imwrite(file_name + ".jpg", frame)          # capture close moment
                break

        subprocess.call(cmd.split())

        capture.release()
        cv2.destroyAllWindows()


# if __name__ == '__main__':
    # aaa = camera_oneshot_class()
    # bbb = aaa.camera_oneshot()


import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")


def detectface(img):
    img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    images = face_cascade.detectMultiScale(img_gray)

    for x,y,w,h in images:
        face=img[y:y+h,x:x+w]
        face_gray=img_gray[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(face_gray)

        half_face=face.shape[0]//2
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)


mv= cv2.VideoCapture(0)
while True:
    ch,frame=mv.read()
    if ch==True:
        size=(640,480)
        frame=cv2.resize(frame,size)
        detectface(frame)
        cv2.imshow('movie', frame)

    k=cv2.waitKey(1)
    if k==27:
        break

mv.release()
cv2.destroyAllWindows()
