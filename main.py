from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from urllib.parse import urlparse,urlencode
import ipaddress
import re
from feature import featureExtraction


app = Flask(__name__)
model = pickle.load(open('MLP1.pickle', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = str(request.form['URL'])
        print(url)
        URL = []
        URL = featureExtraction(url)
        print(URL)
        prediction = model.predict([URL])
        output = prediction[0]
        print(output)
        if output == 0:
            return render_template('index.html', predictions_texts="NOT A PHISHING WEBSITE")
        else:
            return render_template('index.html', prediction_text="PHISHING WEBSITE !!!")

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
