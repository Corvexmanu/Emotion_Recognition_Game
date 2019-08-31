# Serve model as a flask application

import numpy as np
from flask import Flask, request
from keras.models import load_model
import cv2

model = None
app = Flask(__name__)


def loadModel():
    global model
    # model variable refers to the global variable
    model = load_model("./XCEPTION_48_Karol_0.66.hdf5")

def loadimage(path, verbose = False):
    image = cv2.imread(path)
    image =cv2.resize(image,(48,48))    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = np.expand_dims(image, -1).astype('float64')
    image -= np.mean(image, axis=0)
    image /= np.std(image, axis=0)
    X = []
    X.append(image)
    X = np.array(X)
    return X    

def makePrediction(model,image_to_predict):
  yhat= model.predict(image_to_predict)
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
        data = request.get_data()  # Get data posted as a json 
        # print(data)
        path = "./" + str(data.decode("utf-8"))
        # return path
        x = loadimage(path)
        prediction = makePrediction(model,x)  # runs globally loaded model on the data
    return str(prediction)


if __name__ == '__main__':
    loadModel()  # load model at the beginning once only
    app.run(host='localhost', port=5000)