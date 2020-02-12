# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:49:37 2019

@author: Student
"""



import numpy as np

def ArrayMul(a,kernel):
    b=np.zeros((len(a)-2))
    for x in range(len(b)):        
        b[x]=np.dot((np.array([a[x],a[x+1],a[x+2]])),kernel)
    return b

a=np.array([0,1,0,0,1,0,0,0])
kernel=np.array([0,1,0])
print(ArrayMul(a,kernel))