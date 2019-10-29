# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:54:47 2019

@author: corve
"""
import numpy as np
import cv2
import glob

def storeKarolinska(path1):
    #Exporting to .npy file data from folder containing KDEF Karolinska images
    images = [cv2.imread(file) for file in glob.glob(path1)]
    np.save('./Karolinska_224', images)
    print("Numpy array containing Images created")
    
    #Exporting to csv  data from folder containing KDEF Karolinska images
    mylist = [f for f in glob.glob(path1)]
    np.save("./Karolinska_labels",mylist)
    print("Numpy array containing Labels created")