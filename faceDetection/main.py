import tkinter as tk
import library
import add_new
import view_db
import delete_user


def execute():
    frame_path = r"/facedetection_desktopApplication/frame_collect"
    folder_path = r"/facedetection_desktopApplication/photos"
    library.lib.videoFrameCap(frame_path)

    library.lib.loadface(folder_path, frame_path)

def Add_new():
    add_new.Add_new()

def view_attendance():
    library.lib.view_attendance()

def view():
    view_db.View_all_db()

def delete():
    delete_user.Delete_user()


root = tk.Tk()
root.geometry("600x500")

root.title("Attendance System")
root.configure(bg="#1E90FF")


attendance_label = tk.Label(root, text="Smart Attendance System", font=("Helvetica", 25), bg="#1E90FF", fg="white")
attendance_label.pack(padx=20, pady=10)


button_styles = {
    "width": 30,
    "bg": "#FF6347",
    "fg": "white",    # text color for buttons
    "font": ("Helvetica", 12),  # font family
    "relief": "raised",  # Button border style
}

a = tk.Button(root, text='Add New Face', command=Add_new, **button_styles)
b = tk.Button(root, text='Mark Attendance', command=execute, **button_styles)
c = tk.Button(root, text='View Attendance', command=view, **button_styles)
d = tk.Button(root, text='Delete the user', command=delete , **button_styles)

# Adjusting button layout
button_padding = {'padx': 20, 'pady': 10}

a.pack(**button_padding)
b.pack(**button_padding)
c.pack(**button_padding)
d.pack(**button_padding)

root.mainloop()






