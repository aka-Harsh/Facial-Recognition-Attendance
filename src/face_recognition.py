import cv2
import os
import numpy as np

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def load_known_faces(images_path):
    known_faces = []
    known_ids = []

    for filename in os.listdir(images_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            student_id = os.path.splitext(filename)[0]
            image_path = os.path.join(images_path, filename)
            
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            if len(faces) > 0:
                (x, y, w, h) = faces[0]
                face = gray[y:y+h, x:x+w]
                face_resized = cv2.resize(face, (100, 100))
                known_faces.append(face_resized)
                known_ids.append(student_id)
            else:
                print(f"No face found in {filename}. Skipping...")

    return known_faces, known_ids

def recognize_faces(frame, known_faces, known_ids):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    recognized_ids = []
    face_locations = []

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face, (100, 100))
        
        # Use SSIM (Structural Similarity Index) for comparison
        best_score = -1
        best_id = "Unknown"
        for known_face, known_id in zip(known_faces, known_ids):
            score = cv2.matchTemplate(face_resized, known_face, cv2.TM_CCOEFF_NORMED)[0][0]
            if score > best_score:
                best_score = score
                best_id = known_id
        
        if best_score > 0.5:  # Adjust this threshold as needed
            student_id = best_id
        else:
            student_id = "Unknown"
        
        recognized_ids.append(student_id)
        face_locations.append((y, x+w, y+h, x))

    return face_locations, recognized_ids