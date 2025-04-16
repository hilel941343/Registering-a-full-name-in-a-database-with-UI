from tkinter import *
import mysql.connector
from tkinter import messagebox

# Submit function to insert data into MySQL
def submit_form():
    first = firstnameEntry.get()
    last = lastnameEntry.get()
    selected_gender = gender_var.get()

    if not first or not last or not selected_gender:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",        # Change this if your MySQL username is different
            password="root",        # Add your MySQL password if you have one
            database="Registration"
        )
        cursor = conn.cursor()
        query = "INSERT INTO users (first_name, last_name, gender) VALUES (%s, %s, %s)"
        values = (first, last, selected_gender)
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data inserted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Tkinter window
windows = Tk()
windows.title('Personal Registration Form')
windows.geometry('1200x800')  # A bigger starting size
windows.configure(bg='black')
windows.resizable(True, True)  # Allow maximizing

frame = Frame(windows, bg='black')
frame.pack(fill=BOTH, expand=True)  # Makes frame resize with window

# Heading
heading = Label(frame, text='Personal Registration Form', fg='#97ffff', bg='black', font=('Calibre', 20, 'bold'))
heading.place(x=90, y=3)

# First Name
firstname = Label(frame, text='First Name:', fg='#97ffff', bg='black', font=('Calibre', 15, 'bold'))
firstname.place(x=10, y=70)
firstnameEntry = Entry(frame, width=30, borderwidth=2)
firstnameEntry.place(x=240, y=70)

# Last Name
lastname = Label(frame, text='Last Name:', fg='#97ffff', bg='black', font=('Calibre', 15, 'bold'))
lastname.place(x=10, y=110)
lastnameEntry = Entry(frame, width=30, borderwidth=2)
lastnameEntry.place(x=240, y=110)

# Gender
gender = Label(frame, text='Select Gender:', fg='#97ffff', bg='black', font=('Calibre', 15, 'bold'))
gender.place(x=10, y=150)

gender_var = StringVar()
genderRadio1 = Radiobutton(frame, text='Male', variable=gender_var, value='Male', font='Tahoma 13 bold', bg='black', fg='white', selectcolor='black')
genderRadio1.place(x=240, y=150)

genderRadio2 = Radiobutton(frame, text='Female', variable=gender_var, value='Female', font='Tahoma 13 bold', bg='black', fg='white', selectcolor='black')
genderRadio2.place(x=350, y=150)

# Submit Button
submitbtn = Button(frame, text='Submit', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white',
                   cursor='hand2', border=2, font=('#57alf8', 16, 'bold'), command=submit_form)
submitbtn.place(x=200, y=250)

windows.mainloop()
