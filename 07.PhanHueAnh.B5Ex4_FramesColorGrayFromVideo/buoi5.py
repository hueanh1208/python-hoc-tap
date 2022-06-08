# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:23:03 2021

@author: DELL
"""

import cv2
import numpy as np
import speech_recognition as sr

import os

INPUT_VIDEO = '' # HẰNG = lưu tên Video file Input
OUTPUT_DIR = '' 

def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         r.adjust_for_ambient_noise(source, duration=1)
         print("Mời bạn nói...")
         audio_data = r.record(source, duration=5)
         print("Bạn đang nói...")
         try:
             text = r.recognize_google(audio_data,language="vi")
         except:
             text = "bạn nói gì mình không hiểu!" 
         print("Bạn đã nói là: {}".format(text))
    return text
def print_image(img, diff_im): #Thủ tục xếp 2 frames ảnh liền kề: color và gray của Frame cắt ra từ Video gốc 
    """
    đặt các khung hình kế liền nhau = Place images side-by-side
    """
    new_img = np.zeros([img.shape[0], img.shape[1]*2, img.shape[2]]) 
    new_img[:, :img.shape[1], :] = img    # Đặt hình gốc (color) vào ví bên trái (đầu tiên)
    new_img[:, img.shape[1]:, 0] = diff_im # Đặt hình c (color) vào ví bên trái (đầu tiên)
    new_img[:, img.shape[1]:, 1] = diff_im
    new_img[:, img.shape[1]:, 2] = diff_im
    #cv2.imshow('diff', new_img)         # show hình kết quả sau khi ghép (có thể ko cần = tránh làm chậm App) 
    return new_img
#CẮT VIDEO GỐC
def main(video_path):
    cap = cv2.VideoCapture(video_path) # PHÁT VIDEO (LẤY video từ CAM thì ghi 0 = không dùng tham số trên)
    last_gray = None # Biến đối tượng hình Gray (so sánh 2 Frames hình được cắt kế liền nhau)
    idx = -1
    fileName = input("Nhập tên file khi lưu: ")
    
    while(True):
        ret, frame = cap.read() #Cắt các frame hình: hình color cắt được lưu vào frame, ret = giữ vị trí kế tiếp của video (sau khi cắt) 
        cv2.imshow('Khung Hinh', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        idx += 1
        if not ret: #or cv2.waitKey(10) & 0xFF == ord('q'):  #vị trí kế tiếp ko còn nữa (hết Video)
            print('Dừng đọc Video vì đã hết (%s)' % video_path)
            break
        
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if last_gray is None: 
            last_gray = gray
            continue      
        diff = cv2.absdiff(gray, last_gray) 
        cv2.imwrite(os.path.join(OUTPUT_DIR, fileName+'%d.jpg' %idx), print_image(frame, diff)) 
        last_gray = gray 
        print('Lưu hình thứ :  @ %d...' % idx)
        pass
    pass
    
    cap.release() #Giải phóng biến đối tượng Video cap 
    cv2.destroyAllWindows() # Đóng tất cả các cửa số
x =True
while x:
    print (""" 
               1. Nạp video
               2.Thoát
           """)
    hueanh07 = input("Chọn: ")
    if hueanh07 == "1":
        #in danh sách các file video
        print('''
              Danh sách các file:
              1. HongKong.mp4
              2. Jeju3.MOV
              3. JejuDocNguoc.MOV
              
              ''')
        a = True
        while a:
            
            print ('''
                Chọn các chức năng
               1. Nạp bằng cách nhập số thứ tự
               2. Dùng giọng nói
               3. Video từ camera
               4. Thoát
               ''')
            hueanh = input("chọn: ")
            #nhập
            if  hueanh == "1":
                nhap = input("Chọn số thứ tự: ")
                if nhap == "1":
                    tenfile = 'HongKong.mp4'
                    INPUT_VIDEO = tenfile
                    a = None
                if nhap == "2":
                    tenfile = 'Jeju3.MOV'
                    INPUT_VIDEO = tenfile
                    a = None
                if nhap == "3":
                    tenfile = 'JejuDocNguoc.MOV'
                    INPUT_VIDEO = tenfile
                    a = None
                
                
                    
            #voice
            elif hueanh == "2":
                y=True
                while y == True:
                    # lấy tên file
                    text_voice = voice()
                    if text_voice == "một":
                        tenfile = 'HongKong.mp4'
                        print(tenfile)
                        INPUT_VIDEO = tenfile
                        y=False
                        a= None
                    elif text_voice == "hai":
                        tenfile = 'Jeju3.MOV'
                        INPUT_VIDEO = tenfile
                        y=False
                        a= None
                    elif text_voice == "ba":
                        tenfile = "JejuDocNguoc.MOV"
                        INPUT_VIDEO = tenfile
                        y=False
                        a= None
            elif hueanh == "4":
                tenfile = 0
                INPUT_VIDEO = tenfile
                a= None
            else: 
                a= None
                print("Tạm biệt")
        OUTPUT_DIR = input("Nhập tên thư mục để lưu ảnh")
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        print('Chạy chương trình với video clip %s' % INPUT_VIDEO)
        main(video_path=INPUT_VIDEO)
        list_img = os.listdir(OUTPUT_DIR) #lấy path các file hình ảnh
        b = True
        while b:
            print (""" 
                       
                       1. Cắt khung ảnh
                       2. Quay ảnh
                       3. Co dãn hình ảnh
                       4. Thoát
                   """)
            hueanh = input("Chọn: ")
          
                      
            if hueanh == "1":
                # cắt ảnh
                h_s = int(input("Nhập chiều cao bắt đầu: "))
                h_e = int(input("Nhập chiều cao kết thúc: "))
                w_s = int(input("Nhập chiều rộng bắt đầu: "))
                w_e = int(input("Nhập chiều rộng kết thúc: "))
                          
                cut = input("Nhập tên thư mục để lưu: ")
                os.makedirs(cut, exist_ok=True)
                dem = 0
                for img in list_img:
                    img_cut = os.path.join(OUTPUT_DIR,img)
                    r = cv2.imread(img_cut)
                    i = r[h_s:h_e, w_s:w_e]
                    cv2.imwrite(os.path.join(cut, "cut%d.jpg" %dem), i)
                    dem = dem +1
                    
            elif hueanh == "2":
                do = int(input("Nhập độ xoay: "))
                rota = input("Nhập tên thư mục để lưu: ")
                os.makedirs(rota, exist_ok=True)
                dem = 0
                for img in list_img:
                     img_rota = os.path.join(OUTPUT_DIR,img)
                     img_ = cv2.imread(img_rota) 
                     (h, w, d) = img_.shape 
                     center = (w // 2, h // 2) 
                     M = cv2.getRotationMatrix2D(center, do, 1.0) 
                     rotated = cv2.warpAffine(img_, M, (w, h))
                     cv2.imwrite(os.path.join(rota, "rota%d.jpg" %dem), rotated)
                     dem = dem + 1
            elif hueanh == "3":
                resize = input("Nhập thư mục để lưu: ")
                size = int(input("Nhập tỉ lệ: :"))
                os.makedirs(resize, exist_ok=True)
                dem =0
                for img in list_img:
                    img_re = os.path.join(OUTPUT_DIR,img)
                    img_ = cv2.imread(img_re) 
                    (h, w, d) = img_.shape 
                    r = float(size) / w 
                    dim = (size, int(h * r))
                    resized = cv2.resize(img_, dim)
                    cv2.imwrite(os.path.join(resize, "resize%d.jpg" %dem),resized)
                    dem = dem + 1               
            else:
                b = None
                print("Tạm biệt")
            

    else:
        x = None
        print("Tạm biệt")
        
        


                