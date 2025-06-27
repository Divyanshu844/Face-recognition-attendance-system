# Face-recognition-attendance-system
# 🎯 Face Recognition Attendance System

A Python-based desktop application that automates the student attendance process using real-time facial recognition. This system uses **OpenCV**, **Tkinter**, **MySQL**, and **CSV** integration to provide a seamless, contactless attendance experience for institutions.

---

## 📸 Features

- 🎓 Student registration with photo capture
- 🤖 Real-time face detection and recognition
- 🧠 Trains model using **LBPH (Local Binary Patterns Histogram)**
- 🗂️ Attendance marking with date and time
- 🧾 Export/import attendance records as CSV
- 📋 GUI for managing students and attendance
- 💾 Integration with **MySQL database**

---

## 🛠️ Tech Stack

| Component     | Technology                     |
|---------------|--------------------------------|
| GUI           | Tkinter (Python Standard GUI)  |
| Face Detection| OpenCV with Haar Cascade       |
| Recognition   | LBPH Face Recognizer (OpenCV)  |
| Database      | MySQL                          |
| Image Handling| Pillow (PIL)                   |
| Data Storage  | CSV files                      |

---

## 📁 Project Structure

FaceRecognitionAttendance/
├── data/ # Captured student images
├── haarcascade_frontalface_default.xml
├── classifier.xml # Trained LBPH model
├── divyanshu.csv # Attendance log (CSV format)
├── student.py # Student management module
├── train.py # Training model script
├── face_recognition_data.py # Face detection & recognition logic
├── attendance.py # Attendance tracking and GUI
├── main.py # Main GUI application
└── images/ # UI images and icons



Install 

pip install opencv-python
pip install pillow
pip install mysql-connector-python

Database

CREATE DATABASE face_recognizer;
USE face_recognizer;

CREATE TABLE student (
    Student_id VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100),
    Roll VARCHAR(100),
    Dep VARCHAR(100)
);

