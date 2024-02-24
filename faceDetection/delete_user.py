
import mysql.connector
import tkinter as tk
from tkinter import messagebox


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'abc123',
    database = 'attendance'
)
cursor = mydb.cursor()



def delete_person(root, name_entry):
    person_name = name_entry.get()

    sql = 'DELETE FROM persons WHERE pname = (%s) AND EXISTS (SELECT 1 FROM persons WHERE pname = (%s))'
    values = (person_name, person_name)

    cursor.execute(sql, values)
    mydb.commit()

    messagebox.showinfo("Person Deleted", f"{person_name} deleted successfully!")
    root.destroy()


def delete_all(root):






    messagebox.showinfo("All Persons Deleted", "All persons deleted successfully!")

def Delete_user():
    root = tk.Tk()

    root.geometry('400x300')
    root.title("Delete User")
    root.configure(bg="#1E90FF")

    def open_delete_person_window():
        delete_person_window = tk.Toplevel(root)
        delete_person_window.geometry('400x300')
        delete_person_window.configure(bg="#1E90FF")

        label = tk.Label(delete_person_window, text='Enter the name of the person to delete')
        label.pack(pady=10)

        name_entry = tk.Entry(delete_person_window)
        name_entry.pack(pady=10)

        delete_button = tk.Button(delete_person_window, text='Delete Person', command=lambda: delete_person(delete_person_window, name_entry))
        delete_button.pack(pady=10)

    delete_person_button = tk.Button(root, text='Delete a person', command=open_delete_person_window)
    delete_all_button = tk.Button(root, text='Delete all', command=lambda: delete_all(root))

    button_padding = {'padx': 20, 'pady': 10}

    delete_person_button.pack(**button_padding)
    delete_all_button.pack(**button_padding)

    root.mainloop()


