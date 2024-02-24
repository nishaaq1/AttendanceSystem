import tkinter as tk
import os
import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'abc123',
    database = 'attendance'
)
cursor = mydb.cursor()

def view_all_person(root):
    for widget in root.winfo_children():
        widget.destroy()

    cursor.execute("SELECT * FROM persons")
    rows = cursor.fetchall()

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    mylist = tk.Listbox(root, yscrollcommand=scrollbar.set)

    for row in rows:
        mylist.insert(tk.END, row)
    mylist.pack(padx=50, pady=50, expand=True)
    scrollbar.config(command=mylist.yview)

def view_attendance(root):
    # Clear all labels inside the root window
    for widget in root.winfo_children():
        widget.destroy()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    mylist = tk.Listbox(root, yscrollcommand=scrollbar.set)

    for row in rows:
        mylist.insert(tk.END, row)
    mylist.pack(padx=50, pady=50, expand=True)
    scrollbar.config(command=mylist.yview)



def View_all_db():
    root = tk.Tk()
    root.geometry('400x300')
    root.title("View Database")
    root.configure(bg="#1E90FF")

    a = tk.Button(root, text='View all persons', command=lambda: view_all_person(root))
    b = tk.Button(root, text='View Attendance', command=lambda: view_attendance(root))

    button_padding = {'padx': 20, 'pady': 10}

    a.pack(**button_padding)
    b.pack(**button_padding)
    root.mainloop()



