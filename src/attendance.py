import pandas as pd
from datetime import datetime

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

def update_attendance(df, recognized_names):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for name in recognized_names:
        if name != "Unknown":
            df.loc[df['Student Name'] == name, 'Status'] = 'Present'
            df.loc[df['Student Name'] == name, 'Last Seen'] = current_time
    return df

def save_attendance(df, csv_path):
    df.to_csv(csv_path, index=False)