# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:03:09 2019

@author: Student
"""
# example of calculation 1d convolutions from numpy
import numpy as np 
#from numpy import asarray 
a=np.array([[-5,2,3,3],[1,2,4,5],[1,2,1,4]])
a[0][0]=-5
b=a[0:1,0:2]

print (b)
'''
print (a.shape)
print (a)
'''