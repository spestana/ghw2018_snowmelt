# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 16:07:11 2018

@author: cristn
"""

import scipy.io
mat = scipy.io.loadmat('veg_bin30res.mat')
data = mat.get("veg_bin30res")
mat = scipy.io.loadmat('veg_bin30res.mat')
#%%
snow_depth = scipy.io.loadmat('snow_depth_30m_2014_2017_r.mat')