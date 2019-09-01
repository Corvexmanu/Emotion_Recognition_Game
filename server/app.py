# Serve model as a flask application

import numpy as np
from flask import Flask, request
from keras.models import load_model
from flask_cors import CORS
import cv2

model = None
app = Flask(__name__)
cors = CORS(app)


def loadModel():
    global model
    # model variable refers to the global variable
    model = load_model("./MY_48_Fer_0.67_bal.hdf5")


def loadimage(path, verbose=False):
    image = cv2.imread(path)
    image = cv2.resize(image, (48, 48))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = np.expand_dims(image, -1).astype('float64')
    image -= np.mean(image, axis=0)
    image /= np.std(image, axis=0)
    X = []
    X.append(image)
    X = np.array(X)
    return X


def makePrediction(model, image_to_predict):
    yhat = model.predict(image_to_predict)
    yh = yhat.tolist()
    count = 0
    for value in yh[0]:
        count = count + 1
        if count == 1:
            print("Angry    = " + "\t" + str(round(value*100)) + "%")
        elif count == 2:
            print("Disgust  = " + "\t" + str(round(value*100)) + "%")
        elif count == 3:
            print("Fear     = " + "\t" + str(round(value*100)) + "%")
        elif count == 4:
            print("Happy    = " + "\t" + str(round(value*100)) + "%")
        elif count == 5:
            print("Sad      = " + "\t" + str(round(value*100)) + "%")
        elif count == 6:
            print("Surprise = " + "\t" + str(round(value*100)) + "%")
        elif count == 7:
            print("Neutral  = " + "\t" + str(round(value*100)) + "%")
    return yh[0]


@app.route('/')
def home_endpoint():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def get_prediction():
    image_data = request.get_data()  # Get data posted as a json

    # return path
    # x = loadimage(image_data)
    # runs globally loaded model on the data
    # prediction = str(makePrediction(model, x))
    response = str([3, 4])

    return response


if __name__ == '__main__':
    loadModel()  # load model at the beginning once only
    app.run(host='localhost', port=5000)
