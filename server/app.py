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
    model._make_predict_function()


def loadimage(image, verbose = False):
    image = np.array(image.split(','))
    image = image.astype('float32')
    image = np.reshape(image,(240,240,4))
    # cv2.imshow('j',image)
    # cv2.waitKey()
    image = image[:, :, 0:3]
    image =cv2.resize(image,(48,48))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("./Test.jpg", image)
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
    # Works only for a single sample
    if request.method == 'POST':
        data = request.get_data()  # Get data posted   
        image = data.decode("utf-8")             
        x = loadimage(image)
        prediction = makePrediction(model,x)  # runs globally loaded model on the data
    return str(prediction)


if __name__ == '__main__':
    loadModel()  # load model at the beginning once only
    app.run(host='localhost', port=5000)
