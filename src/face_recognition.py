import face_recognition
import cv2
import os
import numpy as np

def load_known_faces(images_path):
    known_faces = []
    known_names = []

    for filename in os.listdir(images_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image = face_recognition.load_image_file(os.path.join(images_path, filename))
            encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(encoding)
            known_names.append(os.path.splitext(filename)[0])

    return known_faces, known_names

