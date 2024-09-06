import streamlit as st
import cv2
import pandas as pd
import os
from datetime import date
from face_recognition import load_known_faces, recognize_faces
from src.attendance import load_daily_attendance, update_attendance, save_daily_attendance, get_attendance_summary
