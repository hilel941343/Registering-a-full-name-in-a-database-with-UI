# Registering-a-full-name-in-a-database-with-UI

# 📌 Overview
This project is a personal registration system built with Python (Tkinter) for the graphical interface and MySQL for data storage.
It allows users to submit their personal information (first name, last name, gender) and provides the ability to update existing records based on a user ID.

# 🎯 Features
✅ Intuitive and styled Graphical User Interface using Tkinter

✅ Insert new user data into a MySQL database

✅ Update existing user information by ID

✅ Input validation to ensure all fields are filled

✅ Error handling with informative message boxes

✅ Responsive and centered layout for better user experience

🛠 Technologies Used
Python – Core programming language

Tkinter – For creating the desktop GUI

MySQL – As the backend database

mysql-connector-python – For database communication

# 📷 GUI Preview
(Optional: Add a screenshot of the GUI here for better presentation)

# 🧠 How It Works
The user enters their first name, last name, and selects gender.

Clicking Submit will:

Validate input

Connect to the MySQL database

Insert the data into a table called users

If the user wants to update an existing entry:

They must enter the User ID

The new values for the fields

Clicking Update will update the corresponding database row

Appropriate messages are shown for success, validation errors, or database issues.

