# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:06:11 2019

@author: corve
"""

#Loading the required Libraries
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from keras.layers import Dense
from keras.layers import GlobalAveragePooling2D
from keras.models import Model
from keras.applications import xception

def create_model_transfer(shape = (224,224,3), num_labels= 6):
  
  # Tensorflow requires channels in the last for input shape
  model = xception.Xception(weights='imagenet', include_top=False, input_shape=shape)

  # New Layers which will be trained on our data set and will be stacked over the Xception Model
  x=model.output
  x=GlobalAveragePooling2D()(x)
  x=Dense(1024,activation='relu')(x)
  x=Dense(512,activation='relu')(x)
  output=Dense(num_labels,activation='softmax')(x)  
  
  #Consolidating the final model
  New_Model=Model(model.input,output)  
  return New_Model

