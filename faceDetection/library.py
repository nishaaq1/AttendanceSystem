import cv2
import os
import face_recognition
import mysql.connector
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'abc123',
    database = 'attendance'
)
cursor = mydb.cursor()


class lib:
    def videoFrameCap(frame_path):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error Accessing the camera")
        else:
            count = 0
            ret = True

            while count<5:
                ret, frame = cap.read()
                frames = os.path.join(frame_path, f'frame{count}.jpg')
                cv2.imwrite(frames, frame)
                count += 1
                cv2.imshow('Capturing Frames', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()



    def loadface(folder_path,frame_path) :
        count = 0

        known_face = os.listdir(folder_path)

        known_encodings = []
        unknown_encodings = []



        for file_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, file_name)
            image = face_recognition.load_image_file(image_path)
            encoding1 = face_recognition.face_encodings(image)
            if len(encoding1) > 0:
                known_encodings.append(encoding1[0])

        for file_name in os.listdir(frame_path):
            image_path = os.path.join(frame_path, file_name)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)
            count = 0
            if len(encoding) > 0:
                unknown_encodings.append(encoding[0])
            else:
                count += 1
                if count>4:
                    root = tk.Tk()
                    a = tk.Label(root, text="No face found")
                    a.pack()
                    root.after(2000, root.destroy)  # to close the Tkinter window after 3 seconds

                    root.mainloop()





        for i in unknown_encodings:
            results = face_recognition.compare_faces(known_encodings, i)

            if True in results:

                index = results.index(True)
                matched_file = known_face[index]

                current_time = datetime.now().strftime('%H:%M:%S')
                status = "present"
                sql = "INSERT INTO students(student_name,Timeof,Attendance) VALUES (%s, %s, %s)"
                values = (matched_file, current_time, status)
                cursor.execute(sql, values)
                mydb.commit()


                break
            else:

                count += 1
                if count >= 4:
                    root = tk.Tk()
                    a = tk.Label(root, text="Your photo did not match with the dataset or look at the camera properly")
                    a.pack()
                    root.after(5000, root.destroy)  #to close the Tkinter window after 3 seconds

                    root.mainloop()













