#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 16:12:19 2018

@author: caser
"""

#1 importnumpy and pandas
import numpy as np
import pandas as pd
import glob
import scipy.io as sio

#2 import data from a csv files
path_list=glob.glob('*/*.csv')
file_count=len(path_list)

for i in range(file_count):
    df=pd.read_csv(path_list[i],delimiter=";",decimal=',', skiprows=(0,1,2,3,4,5,6,7,8,9,10,11,13))
    file_name=str(path_list[i])[6:-4]
    df.to_csv(file_name)
  


#sio.savemat(file_name, mdict={'df': df})

#a=glob.glob('*/*.csv')
#inp1=pd.read_csv(a[2], delimiter=";", decimal = ',',skiprows=(0,1,2,3,4,5,6,7,8,9,10,11,13))




##2 import data from a csv files
#path = "./input/"
#path_list= glob.glob(os.path.join(path, "*.csv")) #make list of paths
#
##file_name = os.path.splitext(os.path.basename('./input/AV96001_cBoltc01_CT_3.csv'))[0]
#df=pd.read_csv(*/input/AV96001_cBoltc01_CT_3.csv)
#
#for i in path_list:
#    df=pd.read_csv(i)
#    file_name = os.path.splitext(os.path.basename(i))[0]
#    sio.savemat(file_name+'.mat', {'a_dict': df})
#    
#    # Getting the file name without extension
#    file_name = os.path.splitext(os.path.basename(file))[0]
#    # Reading the file content to create a DataFrame
#    a='df_'+str(file)
#    a = pd.read_csv(file)
    