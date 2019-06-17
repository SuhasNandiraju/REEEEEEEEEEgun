import face_recognition
import cv2
import numpy as np
import serial
import time

arduino = serial.Serial('/dev/cu.usbmodem14201', 9600)

video_capture = cv2.VideoCapture(1)

you_image = face_recognition.load_image_file("obama.jpg")
you_face_encoding = face_recognition.face_encodings(you_image)[0]

friend_image = face_recognition.load_image_file("biden.jpg")
friend_face_encoding = face_recognition.face_encodings(friend_image)[0]


known_face_encodings = [
    you_face_encoding,
    friend_face_encoding,

]
known_face_names = [
    "you",
    "your friend",
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    #process_this_frame = not process_this_frame

    astr = '1'
    '''
    if 'Unknown' in face_names:
        arduino.write('0')
    else:
        arduino.write('1')
        '''
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)


        if left < 300:
            astr = '3'
        elif left > 600:
            astr = '2'
        else:
            astr = '0'

        print(left)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    arduino.write(astr)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
