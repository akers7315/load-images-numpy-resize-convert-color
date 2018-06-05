# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:21:58 2018

@author: rober
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/python

import glob
import cv2
import numpy as np

X = []

for filename in glob.glob('file-path\\*.jpg'): #assuming gif
    img = cv2.imread(filename)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized_img = cv2.resize(gray_img, (200, 200))
    
    X.append(resized_img)

X = np.asarray(X)
print(X.shape)
