from __future__ import print_function
import os
import sys
import re
import csv
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC,LinearSVC
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pandas as pd
from flask import Flask, render_template, request, send_from_directory, url_for, redirect, flash ,jsonify
from werkzeug.utils import secure_filename
import tweepy
import json
from flask import json
from flask import Flask, request, jsonify

import codecs
from dateutil import parser
header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
import urllib3 

UPLOAD_FOLDER = 'data'
ALLOWED_EXTENSIONS = set(['csv','xlsx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename): # allowed function type extention data
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# TEMPLATE 
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/tweet", methods=['GET','POST'])
def tweet():
    if request.method == "POST":
        dataUrl = request.files['csvfile']
        filename = "data.csv"
        fileLocation = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        dataUrl.save(fileLocation)
        df = pd.read_csv(f"{fileLocation}")
        results = []
        for i in df.index:
            data = {}
            data['tweet'] = df['tweet'][i]
            data ['tweet_preprocessing'] = df['tweet_preprocessing'][i]
            data ['sentimen'] = df ['sentimen'][i]
            results.append(data)
        # return render_template("tweet.html")
        # output = []
        # for item in results:
        #     output.append({
        #         "tweet":item["tweet"],
        #         "tweet_preprocessing":item["tweet_preprocessing"],
        #         "sentimen":item["sentimen"]
        #     })

        # print(output)
        return render_template("tweet.html", data=results)
    return render_template("tweet.html")
      
@app.route('/data', methods=['GET','POST'])
def data():        
    return render_template("data.html",results=results)

@app.route("/preprocessing")
def preprocessing():
    return render_template('preprocessing.html')

@app.route("/classification")
def classification():
    return render_template('classification.html')

@app.route("/nbr")
def nbr():
    return render_template('nbr.html')



if __name__ == "__main__":
    app.run(debug = True)
