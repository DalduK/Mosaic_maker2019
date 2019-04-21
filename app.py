from flask import Flask
from flask import request,send_file
from random import shuffle
import re
import urllib
import numpy as np
import cv2
import os

app = Flask(__name__)


@app.route('/mozaika')
def get():
    losowo = request.args.get('losowo',type=int)
    rozdzielczosc = request.args.get('rozdzielczosc',default="2048x2048",type=str)
    zdjecie = request.args.get('zdjecie',type=str)
    if re.search("\d+"+"x"+"\d+",rozdzielczosc):
        rozdzielczosc = rozdzielczosc
    else:
        rozdzielczosc = "2048x2048"
    r = rozdzielczosc.split("x")
    s1 = int(r[0])
    s2 = int(r[1])
    g = zdjecie.split(",")
    zdjecia = []
    zdjecia2 = []
    if losowo == 1:
        shuffle(g)
    h = len(g)
    for i in range(h):
        req = urllib.request.urlopen(
            g[i])
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        zdjecia.append(img)
    cols = zdjecia[0].shape[0]
    rows = zdjecia[0].shape[1]
    border_h = 0
    border_v = 0
    for i in range(h):
        img = cv2.resize(zdjecia[i],(rows,cols))
        zdjecia2.append(img)
    if h == 1:
        colf2 = cv2.resize(zdjecia[0], (s1, s2))
    elif h == 2:
        colf = np.hstack([zdjecia[0], zdjecia2[1]])
        colf2 = cv2.resize(colf, (s1, s2))
    elif h == 3:
        col1 = np.vstack([zdjecia[0]])
        col2 = np.vstack([zdjecia2[1], zdjecia2[2]])
        if (col2.shape[0] / col2.shape[1]) >= (col1.shape[0] / col1.shape[1]):
            border_v = int((((col2.shape[0] / col2.shape[1]) * col1.shape[1]) - col1.shape[0]) / 2)
        else:
            border_h = int((((col2.shape[0] / col2.shape[1]) * col1.shape[0]) - col1.shape[1]) / 2)
        img = cv2.copyMakeBorder(col1, border_v, border_v, border_h, border_h, cv2.BORDER_CONSTANT, 0)
        col1 = cv2.resize(img, (col2.shape[1], col2.shape[0]))
        colf = np.hstack([col1, col2])
        colf2 = cv2.resize(colf, (s1, s2))
    elif h == 4:
        col1 = np.vstack([zdjecia[0], zdjecia2[1]])
        col2 = np.vstack([zdjecia2[2], zdjecia2[3]])
        colf = np.hstack([col1, col2])
        colf2 = cv2.resize(colf, (s1, s2))
    elif h == 5:
        col1 = np.vstack([zdjecia[0], zdjecia2[1]])
        col2 = np.vstack([zdjecia2[2], zdjecia2[3], zdjecia2[4]])
        if (col2.shape[0] / col2.shape[1]) >= (col1.shape[0] / col1.shape[1]):
            border_v = int((((col2.shape[0] / col2.shape[1]) * col1.shape[1]) - col1.shape[0]) / 2)
        else:
            border_h = int((((col2.shape[0] / col2.shape[1]) * col1.shape[0]) - col1.shape[1]) / 2)
        img = cv2.copyMakeBorder(col1, border_v, border_v, border_h, border_h, cv2.BORDER_CONSTANT, 0)
        col1 = cv2.resize(img, (col2.shape[1], col2.shape[0]))
        colf = np.hstack([col1, col2])
        colf2 = cv2.resize(colf, (s1, s2))
    elif h == 6:
        col1 = np.vstack([zdjecia[0], zdjecia2[1], zdjecia2[2]])
        col2 = np.vstack([zdjecia2[3], zdjecia2[4], zdjecia2[5]])
        colf = np.hstack([col1, col2])
        colf2 = cv2.resize(colf, (s1, s2))
    elif h == 7:
        col1 = np.vstack([zdjecia[0], zdjecia2[1], zdjecia2[2]])
        col2 = np.vstack([zdjecia2[3], zdjecia2[4], zdjecia2[5],zdjecia2[6]])
        if (col2.shape[0] / col2.shape[1]) >= (col1.shape[0] / col1.shape[1]):
            border_v = int((((col2.shape[0] / col2.shape[1]) * col1.shape[1]) - col1.shape[0]) / 2)
        else:
            border_h = int((((col2.shape[0] / col2.shape[1]) * col1.shape[0]) - col1.shape[1]) / 2)
        img = cv2.copyMakeBorder(col1, border_v, border_v, border_h, border_h, cv2.BORDER_CONSTANT, 0)
        col1 = cv2.resize(img, (col2.shape[1], col2.shape[0]))
        colf = np.hstack([col1, col2])
        colf2 = cv2.resize(colf, (s1, s2))
    elif h == 8:
        col1 = np.vstack([zdjecia[0], zdjecia2[1], zdjecia2[2]])
        col2 = np.vstack([zdjecia2[3], zdjecia2[4], zdjecia2[5]])
        col3 = np.vstack([zdjecia2[6], zdjecia2[7]])
        if (col2.shape[0] / col2.shape[1]) >= (col3.shape[0] / col3.shape[1]):
            border_v = int((((col2.shape[0] / col2.shape[1]) * col3.shape[1]) - col3.shape[0]) / 2)
        else:
            border_h = int((((col2.shape[0] / col2.shape[1]) * col3.shape[0]) - col3.shape[1]) / 2)
        img = cv2.copyMakeBorder(col3, border_v, border_v, border_h, border_h, cv2.BORDER_CONSTANT, 0)
        col3 = cv2.resize(img, (col2.shape[1], col2.shape[0]))
        colf = np.hstack([col1, col2, col3])
        colf2 = cv2.resize(colf, (s1, s2))
    else:
        return "Zbyt wiele argumentow Zdjecie"
    cv2.imwrite("zdjecie.jpg", colf2)
    return send_file("zdjecie.jpg", mimetype='image/jpg')

if __name__ == '__main__':
    app.run()
