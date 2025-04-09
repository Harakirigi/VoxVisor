import cv2
import numpy as np

def recognize_objects(image_bytes, confidence_threshold=0.5, nms_threshold=0.4):
    net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
    
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    
    outs = net.forward(output_layers)
    
    class_ids = []
    confidences = []
    boxes = []

    height, width, _ = img.shape

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confidence_threshold:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)
    
    with open('coco.names', 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    detected_objects = []
    
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            class_id = class_ids[i]
            label = classes[class_id]
            confidence = confidences[i]

            detected_objects.append({
                'label': label,
                'confidence': confidence,
                'box': (x, y, w, h)
            })
    
    return detected_objects