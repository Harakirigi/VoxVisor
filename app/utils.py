import pytesseract
import cv2
import numpy as np
from io import BytesIO

import speech_recognition as sr
# import face_recognition

def recognize_text(image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)
    return text



# Транскрибация аудио в текст
def transcribe_audio(audio_bytes):
    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(audio_bytes, 16000, 2)
    text = recognizer.recognize_google(audio_data)
    return text

# Распознавание лиц
def identify_face(image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    rgb_img = img[:, :, ::-1]
    # face_locations = face_recognition.face_locations(rgb_img)
    # return len(face_locations)
