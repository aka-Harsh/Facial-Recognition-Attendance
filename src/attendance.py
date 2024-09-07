import pandas as pd
from datetime import datetime

def load_attendance(csv_path):
    return pd.read_csv(csv_path)

def update_attendance(df, recognized_names):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for name in recognized_names:
        if name != "Unknown":
            df.loc[df['Student Name'] == name, 'Status'] = 'Present'
            df.loc[df['Student Name'] == name, 'Last Seen'] = current_time
    return df

def save_attendance(df, csv_path):
    df.to_csv(csv_path, index=False)