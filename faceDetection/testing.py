import os
import face_recognition

image1 = face_recognition.load_image_file(r'F:\projects\faceDetection\frame_collect\frame0.jpg')
image2 = face_recognition.load_image_file(r'F:\projects\faceDetection\photos\nithiya.jpeg')


e1 = face_recognition.face_encodings(image1)
e2 = face_recognition.face_encodings(image2)

result = face_recognition.compare_faces([e1[0]],e2[0])

if result:
    print('yes')
else:
    print("not")