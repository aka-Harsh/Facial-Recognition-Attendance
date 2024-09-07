import streamlit as st
import cv2
import pandas as pd
import os
from datetime import date
from face_recognition import load_known_faces, recognize_faces
from attendance import load_daily_attendance, update_attendance, save_daily_attendance, get_attendance_summary

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
    st.subheader(f"Attendance for {selected_date}")
    attendance_df = load_daily_attendance(str(selected_date))
    st.dataframe(attendance_df)
    
    # Download button
    csv = attendance_df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=f'attendance_{selected_date}.csv',
        mime='text/csv',
    )
else:
    st.subheader("Live Face Recognition")
    run = st.checkbox('Start Face Recognition')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)

    while run:
        _, frame = camera.read()
        
        face_locations, recognized_ids = recognize_faces(frame, known_faces, known_ids)
        
        # Draw rectangles and IDs on the frame
        for (top, right, bottom, left), student_id in zip(face_locations, recognized_ids):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, student_id, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame_rgb)

        # Update attendance
        attendance_df = load_daily_attendance(str(selected_date))
        attendance_df = update_attendance(attendance_df, recognized_ids, str(selected_date))
        save_daily_attendance(attendance_df, str(selected_date))

        # Debug information
        st.sidebar.write(f"Recognized IDs: {', '.join(recognized_ids)}")

    camera.release()

# Attendance Summary
st.sidebar.subheader("Attendance Summary")
total, present, absent = get_attendance_summary(str(selected_date))
st.sidebar.write(f"Date: {selected_date}")
st.sidebar.write(f"Total Students: {total}")
st.sidebar.write(f"Present: {present}")
st.sidebar.write(f"Absent: {absent}")