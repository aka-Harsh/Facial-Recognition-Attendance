import streamlit as st
import cv2
import pandas as pd
import os
from datetime import date
from face_recognition import load_known_faces, recognize_faces
from src.attendance import load_daily_attendance, update_attendance, save_daily_attendance, get_attendance_summary
IMAGES_PATH = 'data/images'
ATTENDANCE_CSV = 'data/attendance.csv'

# Constants
IMAGES_PATH = 'data/images'
ATTENDANCE_DIR = 'data/daily_attendance'

# Load known faces
known_faces, known_ids = load_known_faces(IMAGES_PATH)

st.title("Facial Recognition Attendance System")

# Sidebar
st.sidebar.header("Options")
selected_date = st.sidebar.date_input("Select Date", date.today())
show_attendance = st.sidebar.checkbox("Show Attendance")

# Debug information
st.sidebar.subheader("Debug Info")
st.sidebar.write(f"Number of known faces: {len(known_faces)}")
st.sidebar.write(f"Known IDs: {', '.join(known_ids)}")
# Main content
if show_attendance:
    st.subheader("Current Attendance")
    st.dataframe(attendance_df)
else:
    st.subheader("Live Face Recognition")
    run = st.checkbox('Start Face Recognition')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)

    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        face_locations, recognized_names = recognize_faces(frame, known_faces, known_names)
        
        # Draw rectangles and names on the frame
        for (top, right, bottom, left), name in zip(face_locations, recognized_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        FRAME_WINDOW.image(frame)
       #Update attendance
        attendance_df = update_attendance(attendance_df, recognized_names)
        save_attendance(attendance_df, ATTENDANCE_CSV)

    camera.release()

st.sidebar.subheader("Attendance Summary")
st.sidebar.write(f"Total Students: {len(attendance_df)}")
st.sidebar.write(f"Present: {(attendance_df['Status'] == 'Present').sum()}")
st.sidebar.write(f"Absent: {(attendance_df['Status'] == 'Absent').sum()}")