import base64
import cv2
import numpy as np


def to_base64(img):

    image = cv2.imencode('.jpg', img)[1]
    return str(base64.b64encode(image))[2:-1]


def to_image(img):

    img_data = base64.b64decode(img)
    img_array = np.fromstring(img_data, np.uint8)
    return cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)[:, :, 0]
