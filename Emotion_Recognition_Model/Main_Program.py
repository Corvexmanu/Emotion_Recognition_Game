# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:01:38 2019

@author: corve
"""

from Model_Creation import create_model_transfer
from Class_Balancing import underSampling_RGB, overSampling_RGB
from Importing_Dataset import storeKarolinska
#Creating  Xception model

storeKarolinska(path1 = r'D:\KDEF_and_AKDEF\KDEF\**\*jpg' )
Xception_transfer_model = create_model_transfer(shape = (224,224,3), num_labels= 6)
Xception_transfer_model.summary()

