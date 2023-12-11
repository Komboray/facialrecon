##############THIS IS A SECURITY CAMERA SYSTEM THAT DETECTS MOVEMENT##########################################
import cv2
import datetime
import time

#we get the video stream
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(cap.get(3))), int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("video.mp4", fourcc, 20, frame_size)

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # mirror = cv2.flip(gray, 1)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    #we are detecting the people in the frame below then the video starts
    #if the body is detected
    if len(faces) + len(bodies) > 0:
        # we are drawing faces

        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x,y), (x + width, y + height), (255, 0, 0), 3)

        if detection:
            timer_started = False
        else:
            detection = True
            #we have detected something then start
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print("Stop Recording!")
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    #we are drawing faces
    # for (x, y, width, height) in faces:
    #     cv2.rectangle(frame, (x,y), (x + width, y + height), (255, 0, 0), 3)

    out.write(frame)
    cv2.imshow("Camera feed", frame)

    if cv2.waitKey(1) == ord('q'):
        break


out.release() #saves the video
cap.release()
cv2.destroyAllWindows()