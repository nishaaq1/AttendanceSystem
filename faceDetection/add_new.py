import mysql.connector
import tkinter as tk
from tkinter import filedialog
import os

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'abc123',
    database = 'attendance'
)
cursor = mydb.cursor()



uploaded_label = None
name_entry = None

def Add_new():
    global uploaded_label, name_entry  #global for

    root = tk.Toplevel()
    root.geometry("400x300")

    label = tk.Label(root, text='Upload your image. It will store it in the database.\nMake sure to rename your image to your name')
    name_entry = tk.Entry(root)

    uploaded_label = tk.Label(root, text='')

    a = tk.Button(root, text='Upload Image', width=30, command=upload_image)
    name_entry.pack()
    label.pack()
    uploaded_label.pack()

    a.pack(padx=20, pady=10)

def upload_image():

    global uploaded_label, name_entry  # Use the global variables

    names = name_entry.get()
    destination_folder = r'F:\projects\faceDetection\photos'
    file_path = filedialog.askopenfilename(title="Select an image",
                                           filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
    if file_path:
        with open(file_path, 'rb') as source_file:
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(destination_folder, file_name)
            with open(destination_path, 'wb') as destination_file:
                destination_file.write(source_file.read())
        print("Image uploaded successfully.")
        names = name_entry.get()
        uploaded_label.config(text=f'{names} your Image uploaded successfully')

    sql = ("INSERT INTO persons(pname) VALUES (%s)")
    value = (names,)

    cursor.execute(sql,value)
    mydb.commit()




