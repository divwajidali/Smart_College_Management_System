# Student Management System (Python)

## Overview
Student Management System is a beginner-friendly Python project built using Object-Oriented Programming (OOP) and JSON file handling.

This project manages:
- Students
- Teachers
- Attendance
- Marks
- Authentication System

The system contains three roles:
- Admin
- Teacher
- Student

Each role has different permissions and access.

---

# Features

## Admin Features
- Add Students
- Add Teachers
- Delete Students
- View All Students
- View All Teachers

## Teacher Features
- Add Student Marks
- Search Student by ID
- View All Students
- Mark Attendance
- View Today's Attendance

## Student Features
- View Own Profile
- View Own Marks
- View Attendance Percentage

---

# Technologies Used

- Python
- JSON
- OOP (Object-Oriented Programming)
- File Handling
- Datetime Module

---

# Project Structure

```bash
project/
│
├── main.py
├── User.json
├── Student.json
├── Teacher.json
├── Attendance.json
```

---

# JSON Files

## User.json
Stores login and signup information.

Example:

```json
[
    {
        "Name": "Ali",
        "Email": "ali@gmail.com",
        "Password": "12345678",
        "Role": "Student"
    }
]
```

---

## Student.json
Stores student details.

Example:

```json
[
    {
        "ID": "101",
        "Name": "Ali",
        "Age": "20",
        "Email": "ali@gmail.com",
        "Phone no": "03001234567",
        "Course": "BSCS",
        "Marks": "90"
    }
]
```

---

## Teacher.json
Stores teacher details.

Example:

```json
[
    {
        "ID": "201",
        "Name": "Ahmed",
        "Subject": "Python",
        "Salary": "50000"
    }
]
```

---

## Attendance.json
Stores attendance records.

Example:

```json
[
    {
        "ID": "101",
        "Date": "2026-05-18",
        "Status": "Present"
    }
]
```

---

# Attendance System

## How Attendance Works
- Teacher marks attendance using Student ID
- Current date stores automatically
- Same student attendance cannot be marked twice on the same day
- Attendance percentage calculates automatically

---

# Validation Features

- Unique Email Validation
- Unique ID Validation
- Password Length Validation
- Role Validation

---

# Concepts Used

This project uses:
- Classes and Objects
- Inheritance
- Functions
- Loops
- Conditional Statements
- JSON File Handling
- Exception Handling
- Data Validation

---

# Future Improvements

You can improve this project by adding:
- Update Student Feature
- Delete Teacher Feature
- Password Hashing
- GUI Version
- MySQL Database
- Export Reports
- Subject-wise Attendance
- Multiple Courses
- Result System

---

# How To Run

## Step 1
Install Python

## Step 2
Download or clone the project

## Step 3
Open terminal in project folder

## Step 4
Run the project

```bash
python main.py
```

---

# Learning Purpose

This project is created for learning:
- Python OOP
- Real-world project structure
- Authentication systems
- Attendance management systems
- JSON handling
- File handling

---

# Author

Wajid Ali

Python Beginner Developer 🚀