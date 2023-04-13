import requests
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time
import serial
from tensorflow.keras import datasets, layers, models

ser = serial.Serial('COM4', 9600, timeout=1)
class_names = ['apples', 'bottles', 'bowls', 'cans', 'cups', 'oranges', 'pears', 'plates']
model = models.load_model('image_classifier_nice.model')
def take():
    url = "http://192.168.1.116:8080/shot.jpg"
    img = requests.get(url)
    ar = np.array(bytearray(img.content), dtype=np.uint8)
    img = cv.imdecode(ar, -1)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    img = img[700:, 210:900]
    img = cv.resize(img, (32, 32), interpolation = cv.INTER_AREA)
    plt.imshow(img, cmap=plt.cm.binary)
    plt.show()
    return img

def predict(img):
    prediction = model.predict(np.array([img])/255)
    idx = np.argmax(prediction)
    print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(prediction)], 100 * np.max(prediction))
    )
    return idx
def fetch():
    return int(ser.readline().decode().strip())
while(1):
    x = 0
    try: x = fetch()
    except: continue
    if(x == -1):
        time.sleep(0.1)
        continue
    print("predicting")
    res = predict(take())
    if(res in [0, 5, 6]): #organic
        print(f"{class_names[res]}, organic")
        ser.write(b'2')
    else: #anorganic
        print(f"{class_names[res]}, anorganic")
        ser.write(b'3')
    time.sleep(0.2)
