# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:01:38 2019

@author: corve
"""

from Model_Creation import create_model_transfer

#Importing Xception model
Xception_transfer_model = create_model_transfer(shape = (224,224,3), num_labels= 6)
Xception_transfer_model.summary()

