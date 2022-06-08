# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:46:38 2021

@author: DELL
"""

import cv2
hueanh07 = True
while hueanh07: 
    print (""" 
               1. Ảnh màu
               2. Ảnh xám
               3. Thoát
           """)
    hueanh07 = input("Chọn ảnh: ")
        
    if hueanh07 == "1":
        img_name = input("Nhập tên file hình ảnh:")
        img = cv2.imread(img_name)
        chon = True
        while chon:
            print("""
                      1. Chuyển ảnh xám
                      2. Lấy kích thước ảnh
                      3. Cắt ảnh
                      4. Xoay ảnh
                      5. Lấy giá trị màu tại vị trí
                      6. Thay đổi kích thước
                      7. Thoát
                """)
            chon = input("Chọn : ")
            
            if chon == "1":
                img_gray = cv2.imread(img_name,cv2.IMREAD_GRAYSCALE)
                cv2.imshow('image',img_gray)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif chon == "2":
                (h, w, d) = img.shape
                print ("Kích thước hình ảnh là: ")
                print("width={}, height={}, depth={}".format(w, h, d))
            elif chon == "3":
                h_s = int(input("Nhập chiều cao bắt đầu: "))
                h_e = int(input("đến: "))
                w_s = int(input("Nhập chiều rộng bắt đầu: "))
                w_e = int(input("đến: "))
                
                p = img[h_s:h_e, w_s:w_e] 
                cv2.imshow('Region Of Interest', p)
                cv2.waitKey(0)
                
            elif chon == "4":
                (h, w, d) = img.shape 
                r = int(input("Nhập chiều xoay: "))
                center = (w // 2, h // 2) 
                M = cv2.getRotationMatrix2D(center, r, 1.0) 
                rotated = cv2.warpAffine(img, M, (w, h))
                cv2.imshow("image rotate", rotated)
                cv2.waitKey(0)
            elif chon == "5":
                x = int(input("Nhập tọa độ x: "))
                y = int(input("Nhập tọa độ y: "))
                (B, G, R) = img[x, y]
                print("R={}, G={}, B={}".format(R, G, B))
            elif chon == "6":
                (h, w, d) = img.shape
                t = int(input("Nhập tỉ lệ: "))
                r = float(t) / w 
                dim = (t, int(h * r))
                resized = cv2.resize(img, dim)
                cv2.imshow("image resize", resized)
                cv2.waitKey(0)
            elif chon == "7":
                chon = None
                print("Tạm biệt")
            else:
                  print("Vui lòng chọn lại")
                
    
    elif hueanh07 == "2":
        img_name = input("Nhập tên file hình ảnh:")
        img = cv2.imread(img_name)
        chon = True
        while chon:
            print("""
                      1. Lấy kích thước ảnh
                      2. Cắt ảnh
                      3. Xoay ảnh
                      4. Lấy giá trị màu tại vị trí
                      5. Thoát
                """)
            chon = input("Chọn : ")
            if chon == "1":
                (h, w) = img.shape
                print("width={}, height={}".format(w, h)) 
            elif chon == "2":
                h_s = int(input("Nhập chiều cao bắt đầu: "))
                h_e = int(input("Nhập chiều cao kết thúc: "))
                w_s = int(input("Nhập chiều rộng bắt đầu: "))
                w_e = int(input("Nhập chiều rộng kết thúc: "))
                
                p = img[h_s:h_e, w_s:w_e] 
                cv2.imshow('Region Of Interest', p)
                cv2.waitKey(0)
            elif chon == "3":               
                (h, w, d) = img.shape 
                center = (w // 2, h // 2) 
                r = int(input("Nhập chiều xoay: "))
                M = cv2.getRotationMatrix2D(center, r, 1.0) 
                rotated = cv2.warpAffine(img, M, (w, h))
                cv2.imshow("image rotate", rotated)
                cv2.waitKey(0)
            elif chon == "4":
                x = int(input("Nhập tọa độ x: "))
                y = int(input("Nhập tọa độ y: "))
                (B, G, R) = img[x, y]
                print("R={}, G={}, B={}".format(R, G, B))
            elif chon=="5":
                chon = None
                print("Tạm biệt")
            else: 
                print("Vui lòng chọn lại")
    elif hueanh07 == "3":
        hueanh07 = None
        print("Tạm biệt")
    else:
        print("Vui lòng chọn lại")
    
    
        
        
      
        
        
              
    

        

