# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 11:19:50 2021

@author: DELL
"""

import cv2

INPUT_IMAGE = "1.jpg" 




img = cv2.imread(INPUT_IMAGE)
cv2.imshow("Hinh goc",img) 


cv2.waitKey(0)
cv2.destroyAllWindows()