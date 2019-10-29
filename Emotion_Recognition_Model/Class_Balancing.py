# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:50:46 2019

@author: corve
"""
import pandas as pd
import numpy as np
from sklearn.utils import resample

def underSampling(X_train,y_train,ref,cla, shape = (48,48)):
  indexes_ref_cla = np.where(np.logical_or(y_train == ref,y_train == cla))
  X_train_ref_cla = X_train[indexes_ref_cla]
  y_train_ref_cla = y_train[indexes_ref_cla]
  d_ref_cla = {'Image':[np.asarray(row, dtype='float64').reshape(shape[0]*shape[1],1) for row in X_train_ref_cla],'Sentiment':y_train_ref_cla}
  df_ref_cla =pd.DataFrame(d_ref_cla)  
  df_minority_ref_cla=df_ref_cla[df_ref_cla.Sentiment==ref]
  df_majority_ref_cla=df_ref_cla[df_ref_cla.Sentiment==cla]
  df_downsampled_ref_cla = resample(df_majority_ref_cla,replace=False,n_samples=len(df_minority_ref_cla),random_state=42)
  df_train_downs_ref_cla=pd.concat((df_downsampled_ref_cla,df_minority_ref_cla),axis=0)  
  y_train_ref_cla=np.array(df_train_downs_ref_cla['Sentiment'])
  X_list_ref_cla = [np.asarray(row, dtype='float64').reshape(shape[0],shape[1]) for row in df_train_downs_ref_cla['Image']]
  X_train_ref_cla = np.asarray(X_list_ref_cla)
  X_index_ref_cla = np.where(y_train_ref_cla==cla)
  return X_train_ref_cla[X_index_ref_cla]
  
def overSampling(X_train,y_train,ref,cla, shape = (48,48)):
  indexes_ref_cla = np.where(np.logical_or(y_train == ref,y_train == cla))
  X_train_ref_cla = X_train[indexes_ref_cla]
  y_train_ref_cla = y_train[indexes_ref_cla]
  d_ref_cla = {'Image':[np.asarray(row, dtype='float64').reshape(shape[0]*shape[1],1) for row in X_train_ref_cla],'Sentiment':y_train_ref_cla}
  df_ref_cla =pd.DataFrame(d_ref_cla)  
  df_minority_ref_cla=df_ref_cla[df_ref_cla.Sentiment==cla]
  df_majority_ref_cla=df_ref_cla[df_ref_cla.Sentiment==ref]
  df_upsampled_ref_cla = resample(df_minority_ref_cla,replace=True,n_samples=len(df_majority_ref_cla),random_state=42)
  df_train_up_ref_cla=pd.concat((df_upsampled_ref_cla,df_minority_ref_cla),axis=0)  
  y_train_ref_cla=np.array(df_train_up_ref_cla['Sentiment'])
  X_list_ref_cla = [np.asarray(row, dtype='float64').reshape(shape[0],shape[1]) for row in df_train_up_ref_cla['Image']]
  X_train_ref_cla = np.asarray(X_list_ref_cla)
  X_index_ref_cla = np.where(y_train_ref_cla==cla)
  return X_train_ref_cla[X_index_ref_cla]
    
def underSampling_RGB(X_train,y_train,ref,cla, shape = (71,71,3)):
  indexes_ref_cla = np.where(np.logical_or(y_train == ref,y_train == cla))
  X_train_ref_cla = X_train[indexes_ref_cla]
  y_train_ref_cla = y_train[indexes_ref_cla]
  d_ref_cla = {'Image':[np.asarray(row, dtype='float64').reshape(shape[0]*shape[1]*shape[2],1) for row in X_train_ref_cla],'Sentiment':y_train_ref_cla}
  df_ref_cla =pd.DataFrame(d_ref_cla)  
  df_minority_ref_cla=df_ref_cla[df_ref_cla.Sentiment==ref]
  df_majority_ref_cla=df_ref_cla[df_ref_cla.Sentiment==cla]
  df_downsampled_ref_cla = resample(df_majority_ref_cla,replace=False,n_samples=len(df_minority_ref_cla),random_state=42)
  df_train_downs_ref_cla=pd.concat((df_downsampled_ref_cla,df_minority_ref_cla),axis=0)  
  y_train_ref_cla=np.array(df_train_downs_ref_cla['Sentiment'])
  X_list_ref_cla = [np.asarray(row, dtype='float64').reshape(shape[0],shape[1],shape[2]) for row in df_train_downs_ref_cla['Image']]
  X_train_ref_cla = np.asarray(X_list_ref_cla)
  X_index_ref_cla = np.where(y_train_ref_cla==cla)
  return X_train_ref_cla[X_index_ref_cla]
  
def overSampling_RGB(X_train,y_train,ref,cla, shape = (71,71,3)):
  indexes_ref_cla = np.where(np.logical_or(y_train == ref,y_train == cla))
  X_train_ref_cla = X_train[indexes_ref_cla]
  y_train_ref_cla = y_train[indexes_ref_cla]
  d_ref_cla = {'Image':[np.asarray(row, dtype='float64').reshape(shape[0]*shape[1]*shape[2],1) for row in X_train_ref_cla],'Sentiment':y_train_ref_cla}
  df_ref_cla =pd.DataFrame(d_ref_cla)  
  df_minority_ref_cla=df_ref_cla[df_ref_cla.Sentiment==cla]
  df_majority_ref_cla=df_ref_cla[df_ref_cla.Sentiment==ref]
  df_upsampled_ref_cla = resample(df_minority_ref_cla,replace=True,n_samples=len(df_majority_ref_cla),random_state=42)
  df_train_up_ref_cla=pd.concat((df_upsampled_ref_cla,df_minority_ref_cla),axis=0)  
  y_train_ref_cla=np.array(df_train_up_ref_cla['Sentiment'])
  X_list_ref_cla = [np.asarray(row, dtype='float64').reshape(shape[0],shape[1],shape[2]) for row in df_train_up_ref_cla['Image']]
  X_train_ref_cla = np.asarray(X_list_ref_cla)
  X_index_ref_cla = np.where(y_train_ref_cla==cla)
  return X_train_ref_cla[X_index_ref_cla]