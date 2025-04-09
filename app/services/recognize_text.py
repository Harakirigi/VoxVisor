import pytesseract
import cv2
import numpy as np
from io import BytesIO

def recognize_text(image_bytes):
    # Преобразуем байты в изображение OpenCV
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Преобразуем изображение в серый цвет для улучшения точности
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Используем Tesseract для извлечения текста
    text = pytesseract.image_to_string(gray)
    return text
