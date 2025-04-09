import pytesseract
import cv2
import numpy as np
from io import BytesIO

def recognize_text(image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    gray = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)
    
    binary_img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    img = cv2.GaussianBlur(binary_img, (5, 5), 0)
    
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    text = pytesseract.image_to_string(img, lang='eng')
    return text