# import cv2
# import face_recognition
# import numpy as np

# def identify_face(image_bytes):
#     np_arr = np.frombuffer(image_bytes, np.uint8)
#     img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

#     rgb_img = img[:, :, ::-1]

#     face_locations = face_recognition.face_locations(rgb_img)

#     return len(face_locations)
