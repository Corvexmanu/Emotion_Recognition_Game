# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:54:47 2019

@author: corve
"""
import numpy as np
import pandas as pd
import cv2
import glob

def storeKarolinska(path1):
    #Exporting to .npy file data from folder containing KDEF Karolinska images
    images = [cv2.imread(file) for file in glob.glob(path1)]
    np.save('./Karolinska_images', images)
    print("Numpy array containing Images created")
    
    #Exporting to csv  data from folder containing KDEF Karolinska images
    mylist = [f for f in glob.glob(path1)]
    np.save("./Karolinska_labels",mylist)
    print("Numpy array containing Labels created")

#Function created to map labels from  karolinsha labels to category numbers.
def mapping(x):
  if x == 'AN':
    return 0
  elif x == 'DI':
    return 1
  elif x == 'AF':
    return 2
  elif x == 'HA':
    return 3
  elif x == 'SA':
    return 4
  elif x == 'SU':
    return 5
  elif x == 'NE':
    return 6

def importKarolinshaDataImages(path1, path2, size):
  
    x = np.load(path1, allow_pickle=True)
    npimages = [cv2.resize(image,size) for image in x]
    x_images = [image.astype('float64') for image in npimages]
    
    y = np.load(path2, allow_pickle=True)
    y_list = [s[32:34] for s in y]
    y_list[1084] = 'SA'
    y_list[2290] = 'SU'
    y_lables = list(map(mapping, y_list))

    #Removing Neutral labels. 
    x_np = np.asarray(x_images)
    y_np = np.asarray(y_lables)
    y_np_ix = np.where(y_np<6)
    x_np = x_np[y_np_ix]
    y_np = y_np[y_np_ix]
    X = x_np
    
    #Applying standard normalization to the training and testing images.
    X -= np.mean(X, axis=0)
    X /= np.std(X, axis=0)
    
    #Converting the output to an array of 0 and . 
    y = pd.get_dummies(pd.Series(y_np)).as_matrix()

    return X,y