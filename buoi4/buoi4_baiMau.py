# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 18:48:12 2021

@author: DELL
"""


import cv2
 
cap = cv2.VideoCapture(0)

count = 0
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('Khung Hinh', frame)
    cv2.imwrite("Khung%d.jpg" %count, frame)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()