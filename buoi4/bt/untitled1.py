# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 17:29:20 2021

@author: DELL
"""
'''img_gray = cv2.imread(i,cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(os.path.join(gray,"gray%d.jpg" %dem) ,img_gray)
        dem = dem + 1'''
import cv2






    elif chon == "3":
        li = os.listdir(path_gray)
        print("ss", li)
        x = int(input("Nhập tọa độ x của tâm xoay: "))
        y = int(input("Nhập tọa độ y của tâm xoay: "))
        r = int(input("Nhập chiều xoay: "))
        for img in li:
            imPath_gray = os.path.join(path_gray,img)
            im = cv2.imread(imPath_gray)
            (h, w, d) = im.shape 
            #e= cv2.cv2.rotate(r,cv2.cv2.ROTATE_90_CLOCKWISE)
            M = cv2.getRotationMatrix2D((x,y), r, 1.0) 
            rotated = cv2.warpAffine(im, M, (w, h))
             
            cv2.imshow("image rotate")
            cv2.waitKey(0)

pic = 'a/a0.jpg'

i = cv2.imread(pic)
cv2.imshow("img", i)

if chon == "1":
    gray = 'gray'
    os.makedirs(gray, exist_ok=True)
    dem = 0
   
    for img in list_img:
        i = cv2.imread(img)
        img_gray = cv2.imread(i,cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(os.path.join(gray,"gray%d.jpg" %dem) ,img_gray)
        dem = dem + 1
    
i = cv2.imread(img)
        img_gray = cv2.imread(i,cv2.IMREAD_GRAYSCALE)
        cv2.waitKey(0)
    cv2.destroyAllWindows()

'''       
if chon == "1":
    
    os.makedirs('gray', exist_ok=True)
    cap = cv2.VideoCapture(tenfile)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        img_gray = cv2.imread(frame,cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(os.path.join('gray',"gray%d.jpg" %count) , img_gray)
        count = count + 1
        if cv2.waitKey(10) & count == ans:
            break
    cap.release()
    cv2.destroyAllWindows()
'''