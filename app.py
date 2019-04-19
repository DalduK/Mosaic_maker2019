from flask import Flask
from flask import request,send_file
from random import shuffle
import re
import urllib
import numpy as np
import cv2

app = Flask(__name__)


@app.route('/mozaic')
def get():
    losowo = request.args.get('losowo',type=bool)
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
    if losowo == 1:
        shuffle(g)
    h = len(g)
    if h == 1:
        req = urllib.request.urlopen(
            g[0])
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        res = cv2.resize(img, (s1, s2))
        cv2.imwrite("zdjeciekota.jpg", res)
    elif h == 2:
        req = urllib.request.urlopen(g[0])
        req2 = urllib.request.urlopen(
            g[1])
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        arr2 = np.asarray(bytearray(req2.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        img2 = cv2.imdecode(arr2, -1)
        cols = img.shape[0]
        rows = img.shape[1]
        imgr2 = cv2.resize(img2, (rows, cols))
        colf = np.hstack([img, imgr2])
        colf2 = cv2.resize(colf, (s1, s2))
        cv2.imwrite("zdjeciekota.jpg", colf2)
    elif h == 3:
        req = urllib.request.urlopen(g[0])
        req2 = urllib.request.urlopen(
            g[1])
        req3 = urllib.request.urlopen(
            g[2])
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        arr2 = np.asarray(bytearray(req2.read()), dtype=np.uint8)
        arr3 = np.asarray(bytearray(req3.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        img2 = cv2.imdecode(arr2, -1)
        img3 = cv2.imdecode(arr3, -1)
        cols = img.shape[0]
        rows = img.shape[1]
        imgr2 = cv2.resize(img2, (rows, cols))
        imgr3 = cv2.resize(img3, (rows, cols))
        col1 = np.vstack([img])
        col2 = np.vstack([imgr3, imgr2])
        border_h = 0
        border_v = 0
        if (col2.shape[0] / col2.shape[1]) >= (col1.shape[0] / col1.shape[1]):
            border_v = int((((col2.shape[0] / col2.shape[1]) * col1.shape[1]) - col1.shape[0]) / 2)
        else:
            border_h = int((((col2.shape[0] / col2.shape[1]) * col1.shape[0]) - col1.shape[1]) / 2)
        img = cv2.copyMakeBorder(col1, border_v, border_v, border_h, border_h, cv2.BORDER_CONSTANT, 0)
        col1 = cv2.resize(img, (col2.shape[1], col2.shape[0]))
        colf = np.hstack([col1, col2])
        colf2 = cv2.resize(colf, (s1, s2))
        cv2.imwrite("zdjeciekota.jpg", colf2)
    elif h == 4:
        req = urllib.request.urlopen(g[0])
        req2 = urllib.request.urlopen(
            g[1])
        req3 = urllib.request.urlopen(
            g[2])
        req4 = urllib.request.urlopen(g[3])
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        arr2 = np.asarray(bytearray(req2.read()), dtype=np.uint8)
        arr3 = np.asarray(bytearray(req3.read()), dtype=np.uint8)
        arr4 = np.asarray(bytearray(req4.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        img2 = cv2.imdecode(arr2, -1)
        img3 = cv2.imdecode(arr3, -1)
        img4 = cv2.imdecode(arr4, -1)
        cols = img.shape[0]
        rows = img.shape[1]
        imgr2 = cv2.resize(img2, (rows, cols))
        imgr3 = cv2.resize(img3, (rows, cols))
        imgr4 = cv2.resize(img4, (rows, cols))
        col1 = np.vstack([img, imgr2])
        col2 = np.vstack([imgr3, imgr4])
        colf = np.hstack([col1, col2])
        colf2 = cv2.resize(colf, (s1, s2))
        cv2.imwrite("zdjeciekota.jpg", colf2)
    elif h == 5:
        req = urllib.request.urlopen(g[0])
        req2 = urllib.request.urlopen(
            g[1])
        req3 = urllib.request.urlopen(
            g[2])
        req4 = urllib.request.urlopen(g[3])
        req5 = urllib.request.urlopen(g[4])
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        arr2 = np.asarray(bytearray(req2.read()), dtype=np.uint8)
        arr3 = np.asarray(bytearray(req3.read()), dtype=np.uint8)
        arr4 = np.asarray(bytearray(req4.read()), dtype=np.uint8)
        arr5 = np.asarray(bytearray(req5.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        img2 = cv2.imdecode(arr2, -1)
        img3 = cv2.imdecode(arr3, -1)
        img4 = cv2.imdecode(arr4, -1)
        img5 = cv2.imdecode(arr5, -1)
        cols = img.shape[0]
        rows = img.shape[1]
        imgr2 = cv2.resize(img2, (rows, cols))
        imgr3 = cv2.resize(img3, (rows, cols))
        imgr4 = cv2.resize(img4, (rows, cols))
        imgr5 = cv2.resize(img5, (rows, cols))

        col1 = np.vstack([img, imgr2])
        col2 = np.vstack([imgr3, imgr4, imgr5])
        border_h = 0
        border_v = 0
        if (col2.shape[0] / col2.shape[1]) >= (col1.shape[0] / col1.shape[1]):
            border_v = int((((col2.shape[0] / col2.shape[1]) * col1.shape[1]) - col1.shape[0]) / 2)
        else:
            border_h = int((((col2.shape[0] / col2.shape[1]) * col1.shape[0]) - col1.shape[1]) / 2)
        img = cv2.copyMakeBorder(col1, border_v, border_v, border_h, border_h, cv2.BORDER_CONSTANT, 0)
        col1 = cv2.resize(img, (col2.shape[1], col2.shape[0]))
        colf = np.hstack([col1, col2])
        colf2 = cv2.resize(colf, (s1, s2))
        cv2.imwrite("zdjeciekota.jpg", colf2)
    elif h == 6:
        req = urllib.request.urlopen(g[0])
        req2 = urllib.request.urlopen(
            g[1])
        req3 = urllib.request.urlopen(
            g[2])
        req4 = urllib.request.urlopen(g[3])
        req5 = urllib.request.urlopen(g[4])
        req6 = urllib.request.urlopen(
            g[5])
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        arr2 = np.asarray(bytearray(req2.read()), dtype=np.uint8)
        arr3 = np.asarray(bytearray(req3.read()), dtype=np.uint8)
        arr4 = np.asarray(bytearray(req4.read()), dtype=np.uint8)
        arr5 = np.asarray(bytearray(req5.read()), dtype=np.uint8)
        arr6 = np.asarray(bytearray(req6.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        img2 = cv2.imdecode(arr2, -1)
        img3 = cv2.imdecode(arr3, -1)
        img4 = cv2.imdecode(arr4, -1)
        img5 = cv2.imdecode(arr5, -1)
        img6 = cv2.imdecode(arr6, -1)
        cols = img.shape[0]
        rows = img.shape[1]
        imgr2 = cv2.resize(img2, (rows, cols))
        imgr3 = cv2.resize(img3, (rows, cols))
        imgr4 = cv2.resize(img4, (rows, cols))
        imgr5 = cv2.resize(img5, (rows, cols))
        imgr6 = cv2.resize(img6, (rows, cols))
        col1 = np.vstack([img, imgr2, imgr5])
        col2 = np.vstack([imgr3, imgr4, imgr6])
        colf = np.hstack([col1, col2])
        colf2 = cv2.resize(colf, (s1, s2))
        cv2.imwrite("zdjeciekota.jpg", colf2)
    elif h == 7:
        req = urllib.request.urlopen(g[0])
        req2 = urllib.request.urlopen(
            g[1])
        req3 = urllib.request.urlopen(
            g[2])
        req4 = urllib.request.urlopen(g[3])
        req5 = urllib.request.urlopen(g[4])
        req6 = urllib.request.urlopen(
            g[5])
        req7 = urllib.request.urlopen(
            g[6])
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        arr2 = np.asarray(bytearray(req2.read()), dtype=np.uint8)
        arr3 = np.asarray(bytearray(req3.read()), dtype=np.uint8)
        arr4 = np.asarray(bytearray(req4.read()), dtype=np.uint8)
        arr5 = np.asarray(bytearray(req5.read()), dtype=np.uint8)
        arr6 = np.asarray(bytearray(req6.read()), dtype=np.uint8)
        arr7 = np.asarray(bytearray(req7.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        img2 = cv2.imdecode(arr2, -1)
        img3 = cv2.imdecode(arr3, -1)
        img4 = cv2.imdecode(arr4, -1)
        img5 = cv2.imdecode(arr5, -1)
        img6 = cv2.imdecode(arr6, -1)
        img7 = cv2.imdecode(arr7, -1)
        cols = img.shape[0]
        rows = img.shape[1]
        imgr2 = cv2.resize(img2, (rows, cols))
        imgr3 = cv2.resize(img3, (rows, cols))
        imgr4 = cv2.resize(img4, (rows, cols))
        imgr5 = cv2.resize(img5, (rows, cols))
        imgr6 = cv2.resize(img6, (rows, cols))
        imgr7 = cv2.resize(img7, (rows, cols))
        col1 = np.vstack([img, imgr2, imgr5])
        col2 = np.vstack([imgr3, imgr4, imgr7, imgr6])
        border_h = 0
        border_v = 0
        if (col2.shape[0] / col2.shape[1]) >= (col1.shape[0] / col1.shape[1]):
            border_v = int((((col2.shape[0] / col2.shape[1]) * col1.shape[1]) - col1.shape[0]) / 2)
        else:
            border_h = int((((col2.shape[0] / col2.shape[1]) * col1.shape[0]) - col1.shape[1]) / 2)
        img = cv2.copyMakeBorder(col1, border_v, border_v, border_h, border_h, cv2.BORDER_CONSTANT, 0)
        col1 = cv2.resize(img, (col2.shape[1], col2.shape[0]))
        colf = np.hstack([col1, col2])
        colf2 = cv2.resize(colf, (s1, s2))
        cv2.imwrite("zdjeciekota.jpg", colf2)
    elif h == 8:
        req = urllib.request.urlopen(g[0])
        req2 = urllib.request.urlopen(
            g[1])
        req3 = urllib.request.urlopen(
            g[2])
        req4 = urllib.request.urlopen(g[3])
        req5 = urllib.request.urlopen(g[4])
        req6 = urllib.request.urlopen(
            g[5])
        req7 = urllib.request.urlopen(
            g[6])
        req8 = urllib.request.urlopen(g[7])
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        arr2 = np.asarray(bytearray(req2.read()), dtype=np.uint8)
        arr3 = np.asarray(bytearray(req3.read()), dtype=np.uint8)
        arr4 = np.asarray(bytearray(req4.read()), dtype=np.uint8)
        arr5 = np.asarray(bytearray(req5.read()), dtype=np.uint8)
        arr6 = np.asarray(bytearray(req6.read()), dtype=np.uint8)
        arr7 = np.asarray(bytearray(req7.read()), dtype=np.uint8)
        arr8 = np.asarray(bytearray(req8.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        img2 = cv2.imdecode(arr2, -1)
        img3 = cv2.imdecode(arr3, -1)
        img4 = cv2.imdecode(arr4, -1)
        img5 = cv2.imdecode(arr5, -1)
        img6 = cv2.imdecode(arr6, -1)
        img7 = cv2.imdecode(arr7, -1)
        img8 = cv2.imdecode(arr8, -1)
        cols = img.shape[0]
        rows = img.shape[1]
        imgr2 = cv2.resize(img2, (rows, cols))
        imgr3 = cv2.resize(img3, (rows, cols))
        imgr4 = cv2.resize(img4, (rows, cols))
        imgr5 = cv2.resize(img5, (rows, cols))
        imgr6 = cv2.resize(img6, (rows, cols))
        imgr7 = cv2.resize(img7, (rows, cols))
        imgr8 = cv2.resize(img8, (rows, cols))
        col1 = np.vstack([img, imgr2, imgr5])
        col2 = np.vstack([imgr3, imgr4, imgr7])
        col3 = np.vstack([imgr6, imgr8])
        border_h = 0
        border_v = 0
        if (col2.shape[0] / col2.shape[1]) >= (col3.shape[0] / col3.shape[1]):
            border_v = int((((col2.shape[0] / col2.shape[1]) * col3.shape[1]) - col3.shape[0]) / 2)
        else:
            border_h = int((((col2.shape[0] / col2.shape[1]) * col3.shape[0]) - col3.shape[1]) / 2)
        img = cv2.copyMakeBorder(col3, border_v, border_v, border_h, border_h, cv2.BORDER_CONSTANT, 0)
        col3 = cv2.resize(img, (col2.shape[1], col2.shape[0]))
        colf = np.hstack([col1, col2, col3])
        colf2 = cv2.resize(colf, (s1, s2))
        cv2.imwrite("zdjeciekota.jpg", colf2)
    else:
        return "Zbyt wiele argumentow Zdjecie"
    return send_file("zdjeciekota.jpg", mimetype='image/jpg')

if __name__ == '__main__':
    app.run()
