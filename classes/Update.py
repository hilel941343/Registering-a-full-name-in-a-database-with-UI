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
            user="root",
            password="root",
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

# Update function to update data in MySQL
def update_user():
    user_id = idEntry.get()
    first = firstnameEntry.get()
    last = lastnameEntry.get()
    selected_gender = gender_var.get()

    if not user_id or not first or not last or not selected_gender:
        messagebox.showwarning("Input Error", "Please fill in all fields including User ID.")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="Registration"
        )
        cursor = conn.cursor()
        query = "UPDATE users SET first_name = %s, last_name = %s, gender = %s WHERE id = %s"
        values = (first, last, selected_gender, user_id)
        cursor.execute(query, values)
        conn.commit()
        if cursor.rowcount == 0:
            messagebox.showwarning("Not Found", "No user found with this ID.")
        else:
            messagebox.showinfo("Success", "Data updated successfully!")
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Tkinter window
windows = Tk()
windows.title('Personal Registration Form')
windows.geometry('600x500')
windows.configure(bg='black')
windows.resizable(True, True)

frame = Frame(windows, bg='black', padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Heading
heading = Label(frame, text='Personal Registration Form', fg='#97ffff', bg='black', font=('Calibre', 20, 'bold'))
heading.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# User ID for Update
id_label = Label(frame, text='User ID (for update):', fg='#97ffff', bg='black', font=('Calibre', 14, 'bold'))
id_label.grid(row=1, column=0, sticky=E, padx=10, pady=5)
idEntry = Entry(frame, width=30, borderwidth=2)
idEntry.grid(row=1, column=1, padx=10, pady=5)

# First Name
firstname = Label(frame, text='First Name:', fg='#97ffff', bg='black', font=('Calibre', 14, 'bold'))
firstname.grid(row=2, column=0, sticky=E, padx=10, pady=5)
firstnameEntry = Entry(frame, width=30, borderwidth=2)
firstnameEntry.grid(row=2, column=1, padx=10, pady=5)

# Last Name
lastname = Label(frame, text='Last Name:', fg='#97ffff', bg='black', font=('Calibre', 14, 'bold'))
lastname.grid(row=3, column=0, sticky=E, padx=10, pady=5)
lastnameEntry = Entry(frame, width=30, borderwidth=2)
lastnameEntry.grid(row=3, column=1, padx=10, pady=5)

# Gender
gender = Label(frame, text='Select Gender:', fg='#97ffff', bg='black', font=('Calibre', 14, 'bold'))
gender.grid(row=4, column=0, sticky=E, padx=10, pady=5)

gender_var = StringVar()
gender_frame = Frame(frame, bg='black')
gender_frame.grid(row=4, column=1, pady=5)

genderRadio1 = Radiobutton(gender_frame, text='Male', variable=gender_var, value='Male', font='Tahoma 12 bold',
                           bg='black', fg='white', selectcolor='black')
genderRadio1.pack(side=LEFT, padx=10)

genderRadio2 = Radiobutton(gender_frame, text='Female', variable=gender_var, value='Female', font='Tahoma 12 bold',
                           bg='black', fg='white', selectcolor='black')
genderRadio2.pack(side=LEFT, padx=10)

# Buttons
button_frame = Frame(frame, bg='black')
button_frame.grid(row=5, column=0, columnspan=2, pady=20)

submitbtn = Button(button_frame, text='Submit', width=15, borderwidth=5, height=2, bg='#7f7fff', fg='white',
                   cursor='hand2', font=('Tahoma', 12, 'bold'), command=submit_form)
submitbtn.pack(side=LEFT, padx=20)

updatebtn = Button(button_frame, text='Update', width=15, borderwidth=5, height=2, bg='#00cc66', fg='white',
                   cursor='hand2', font=('Tahoma', 12, 'bold'), command=update_user)
updatebtn.pack(side=LEFT, padx=20)

windows.mainloop()
