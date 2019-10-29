# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:01:38 2019

@author: corve
"""

from Model_Creation import create_model_transfer
from Class_Balancing import underSampling_RGB, overSampling_RGB
from Importing_Dataset import storeKarolinska, importKarolinshaDataImages
#Creating  Xception model

storeKarolinska(path1 = r'D:\KDEF_and_AKDEF\KDEF\**\*jpg' )
path_images = './Karolinska_224.npy'
path_labels = './Karolinska_labels.npy'
X,y = importKarolinshaDataImages(path_images,path_labels,(224,224))
Xception_transfer_model = create_model_transfer(shape = (224,224,3), num_labels= 6)
Xception_transfer_model.summary()

