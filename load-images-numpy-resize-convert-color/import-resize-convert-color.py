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
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np

X = []

for filename in glob.glob('C:\\Users\\rober\\OneDrive\\Desktop\\ecchi\\*.jpg'): #assuming gif
    #print (filename)
    img = cv2.imread(filename)
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized_img = cv2.resize(gray_img, (200, 200))
    X.append(resized_img)
    #plt.imshow(resized_img)
    #plt.xticks([]), plt.yticks([]) 
    #plt.show()

X = np.asarray(X)
print(X.shape)