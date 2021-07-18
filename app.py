from __future__ import division, print_function
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import sys
import os
import glob
import re
from faces import faces



app = Flask(__name__)
faces = faces()

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
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        print(file_path)
        
        result = faces.model_predict(img_path=file_path)
        print(str(result))
        return str(result)
    return None


if __name__ == '__main__':
    app.run()