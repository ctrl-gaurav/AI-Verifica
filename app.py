from __future__ import division, print_function
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import sys
import os
import glob
import re
import cv2
import mediapipe as mp


app = Flask(__name__)


def model_predict(img_path):
    print(img_path)
    img = cv2.imread(img_path)

    mpFaceDetection = mp.solutions.face_detection
    mpDraw = mp.solutions.drawing_utils
    faceDetection = mpFaceDetection.FaceDetection(min_detection_confidence=0.20)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    c = 0
    c= int(c)
    if results.detections:
        for id, detection in enumerate(results.detections):
            c=c+1
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            cv2.putText(img, f' {int(detection.score[0] * 100)}%',(bbox[0] - 40, bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 255), 2)

        print("No. of faces Detected : ", c)
        # cv2.imshow("Image", img)
        # cv2.waitKey(0)
    if c>1:
        # print("Your Photo cannot be accepted because there are more than one \nfaces in your uploaded picture")
        return "Your Photo cannot be accepted because there are more than one \nfaces in your uploaded picture\n No. of faces Detected : " + str(c)
    else:
        # print("Tadaa ! Your Photo Has Been Accepted")
        return "Tadaa ! Your Photo Has Been Accepted"


    


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        result = model_predict(file_path)
        print(str(result))
        return str(result)
    return None


if __name__ == '__main__':
    app.run()

