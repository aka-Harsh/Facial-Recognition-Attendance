import pandas as pd
from datetime import datetime
import os

BASE_CSV_PATH = 'data/attendance_base.csv'
ATTENDANCE_DIR = 'data/daily_attendance'

def load_base_attendance():
    if not os.path.exists(BASE_CSV_PATH):
        initialize_base_attendance()
    return pd.read_csv(BASE_CSV_PATH)

def load_daily_attendance(date):
    os.makedirs(ATTENDANCE_DIR, exist_ok=True)
    daily_csv_path = os.path.join(ATTENDANCE_DIR, f'attendance_{date}.csv')
    if not os.path.exists(daily_csv_path):
        base_df = load_base_attendance()
        base_df['Date'] = date
        base_df['Status'] = 'Absent'
        base_df['Last Seen'] = ''
        base_df.to_csv(daily_csv_path, index=False)
    return pd.read_csv(daily_csv_path)

def update_attendance(df, recognized_ids, date):
    current_time = datetime.now().strftime("%H:%M:%S")
    for student_id in recognized_ids:
        if student_id != "Unknown":
            df.loc[df['Student ID'] == int(student_id), 'Status'] = 'Present'
            df.loc[df['Student ID'] == int(student_id), 'Last Seen'] = current_time
    return df

def save_daily_attendance(df, date):
    daily_csv_path = os.path.join(ATTENDANCE_DIR, f'attendance_{date}.csv')
    df.to_csv(daily_csv_path, index=False)

def initialize_base_attendance():
    images_path = 'data/images'
    student_ids = [int(os.path.splitext(f)[0]) for f in os.listdir(images_path) 
                   if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    data = {
        'Student ID': student_ids,
        'Student Name': [f'Student {id}' for id in student_ids],
    }
    df = pd.DataFrame(data)
    df.to_csv(BASE_CSV_PATH, index=False)
    return df

def get_attendance_summary(date):
    df = load_daily_attendance(date)
    total = len(df)
    present = (df['Status'] == 'Present').sum()
    absent = total - present
    return total, present, absent