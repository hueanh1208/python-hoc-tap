# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 09:28:49 2021

@author: DELL
"""

import cv2 as cv
import os
import speech_recognition as sr
import numpy as np

path = "img"


def getFileImg():
    print("""
          1. Nạp file hình ảnh
          2. Chụp ánh từ camera
          
          """)
    ans = input("CHọn: ")
    if ans == "1":
        myList = os.listdir(path) #hinhanh.jpg
            # in list images
        for i in myList:
            print("{} : {}".format(myList.index(i),i))
        print ('''
                    Chọn các chức năng
                   1. Nạp bằng cách nhập số thứ tự
                   2. Dùng giọng nói
                   
                   ''')
        chon = input("Chọn: ")
        if chon == "2":
                
            y=True
            while y == True:
                     
                print("Hãy nói số thứ tự video bạn muốn mở(ví dụ: số 0)")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Adjusting noise ")
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("Nói bằng tiếng Việt đi bạn 5s sau sẽ in ra Text...")
                        # read the audio data from the default microphone
                    audio_data = r.record(source, duration=5)
                    print("Kết quả nhận diện...")
                        # convert speech to text
                    try:
                        text = r.recognize_google(audio_data,language="vi")
                    except:
                        continue 
                   
                    text = text.strip('số ')
                    try:
                        text = int(text)
                        break 
                    except:   
                        continue
            img = cv.imread("{}/{}".format(path,myList[text]))
        elif chon == "1":
            nhap = int(input("Nhập số thứ tự file: "))
            img = cv.imread("{}/{}".format(path,myList[nhap]))
    elif ans == "2":
            
        cam = cv.VideoCapture(0)
        ret, frame = cam.read()  
        while True:
            ret, frame = cam.read()
            cv.imshow("test", frame)
            if not ret:
                break
            k = cv.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "img.jpg"
                cv.imwrite(img_name, frame)
                img = cv.imread(img_name)
                break                  
                
    return img
        
        
def apply_sliding_window(img, kernel, padding=0, stride=1): #padding = số pixel mở rộng ảnh input
                                                            #Stride: khoảng cách trượt.
                                                            #kernel: kích thước cửa sổ trượt
    h, w = img.shape[:2]            # lấy chiều cao & chiều rộng ảnh 
    img_p= np.zeros([h+2*padding, w+2*padding]) # Numpy = lập ma trận trống zero = chiều cao|| rộng + 2 lần pixel mở rộng 
    img_p[padding:padding+h, padding:padding+w] = img # gán ảnh vào khung ma trận nêu trên
    kernel = np.array(kernel) # lập cửa sổ trượt 
    assert len(kernel.shape) == 2 and kernel.shape[0] == kernel.shape[1]    #  assert =kiểm tra đàm bảo (tương tự if) square kernel = số chiều = 2 và 2 chiều bằng nhau
    assert kernel.shape[0] % 2 != 0     # kernel size is odd number = số chiều cao là lè (đương nhiên chiều w cũng lẻ ) = khung vuông 2 chiều có kích thước là số lẻ
    
    k_size = kernel.shape[0] # chiều cao của khung trượt
    k_half = int(k_size/2)   # nửa chiều cao của khung trượt
    
    y_pos = [v for idx, v in enumerate(list(range(k_half, h-k_half))) if idx % stride == 0] # tập vị trí y (dọc)
    x_pos = [v for idx, v in enumerate(list(range(k_half, w-k_half))) if idx % stride == 0] # tập vị trí x (ngang)
    
    new_img = np.zeros([len(y_pos), len(x_pos)]) #lập ma trận khung trồng (chuần bị điền ảnh vào khung trượt) 
    
    for new_y, y in enumerate(y_pos): #chạy vị trí y trong tập vị trí y đã xác định ở trên
        for new_x, x in enumerate(x_pos):  #chạyvị trí x trong tập vị trí x đã xác định ở trên
            if k_half == 0: #bắt đầu điền ảnh từ vị trí 1/2 ảnh đầu (đã xác định ở trên)
                pixel_val = img_p[y, x] * kernel # element-wise multiply = nhân -> mở rộng phần ảnh
            else:
                pixel_val = np.sum(img_p[y-k_half:y-k_half+k_size, x-k_half:x-k_half+k_size] * kernel)  # mở rộng = tích vô hướng 2 vector
            new_img[new_y, new_x] = pixel_val   # gán vị trí ảnh phù hợp vào vị mới => chuẩn trượt tiếp
    return new_img

# HÀM TRƯỢT 3 GAM MÀU = KHÔNG GIAN MÀU RGB
def apply_sliding_window_on_3_channels(img, kernel, padding=0, stride=1):   #làm mờ ảnh 
    layer_blue = apply_sliding_window(img[:,:,0], kernel, padding, stride)
    layer_green = apply_sliding_window(img[:,:,1], kernel, padding, stride)
    layer_red = apply_sliding_window(img[:,:,2], kernel, padding, stride)
    
    new_img = np.zeros(list(layer_blue.shape) + [3])
    new_img[:,:,0], new_img[:,:,1], new_img[:,:,2] = layer_blue, layer_green, layer_red
    return new_img



#GỌI HÀM VỚI THAM SỐ THỰC 

if __name__ == "__main__": 
    img = getFileImg()
    print("""
          1. Nhập tham số
          2. Lựa chon Khung trượt có sẵn
          """)
    OUTPUT_DIR = input("Nhập tên thư mục để lưu ảnh: ")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    chon = input("Chọn: ")
    if chon == "1":
        k = int(input("Nhập kích thước cửa sổ trượt: "))
        p = int(input("Nhập số pixel mở rộng: "))
        s = int(input("Nhập khoảng cách lần trượt: "))
        d = int(input("Nhập khoảng cách của mỗi pixel trên cửa sổ: "))
        fileName = input("Nhập tên file khi lưu: ")    
    
        cv.imshow("Hinh goc",img) 
        new_img = apply_sliding_window_on_3_channels(img, kernel=[[k]], padding=p, stride=s) # làm mở RGB 
        cv.imshow("Hinh moi",new_img) 
        cv.imwrite(os.path.join(OUTPUT_DIR, fileName+'.jpg'), new_img)
        
 
        print('Kich thuoc hinh GOC:', img.shape) # kích thước hình gốc
        print('Kich thuoc hinh moi:', new_img.shape) #kích thước hình mới sau xử lý 
        print('Luu @' ,fileName + ".jpg") # in tên file hình đã lưu
        cv.waitKey(0)
        cv.destroyAllWindows()
        print('------------')
    if chon == "2":
        fileName = input("Nhập tên file khi lưu: ")
        
        lighten_blur_img = apply_sliding_window_on_3_channels(img, kernel=[[0.33, 0.33, 0.33], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33]], padding=1, stride=1)        
        cv.imshow("Hinh lighten_blur",lighten_blur_img)    
        cv.imwrite(os.path.join(OUTPUT_DIR, fileName+'.jpg'), lighten_blur_img)
    
        print('Kích thước hình gốc:', img.shape)
        print('Kích thước sau khi lighten_blur:', lighten_blur_img.shape)
        print('Luu @' ,fileName + ".jpg")
        cv.waitKey(0)
        cv.destroyAllWindows()

list_img = os.listdir(OUTPUT_DIR)
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
            r = cv.imread(img_cut)
            i = r[h_s:h_e, w_s:w_e]
            cv.imwrite(os.path.join(cut, "cut%d.jpg" %dem), i)
            dem = dem +1
                    
    elif hueanh == "2":
        do = int(input("Nhập độ xoay: "))
        rota = input("Nhập tên thư mục để lưu: ")
        os.makedirs(rota, exist_ok=True)
        dem = 0
        for img in list_img:
            img_rota = os.path.join(OUTPUT_DIR,img)
            img_ = cv.imread(img_rota) 
            (h, w, d) = img_.shape 
            center = (w // 2, h // 2) 
            M = cv.getRotationMatrix2D(center, do, 1.0) 
            rotated = cv.warpAffine(img_, M, (w, h))
            cv.imwrite(os.path.join(rota, "rota%d.jpg" %dem), rotated)
            dem = dem + 1
    elif hueanh == "3":
        resize = input("Nhập thư mục để lưu: ")
        size = int(input("Nhập tỉ lệ: :"))
        os.makedirs(resize, exist_ok=True)
        dem =0
        for img in list_img:
            img_re = os.path.join(OUTPUT_DIR,img)
            img_ = cv.imread(img_re) 
            (h, w, d) = img_.shape 
            r = float(size) / w 
            dim = (size, int(h * r))
            resized = cv.resize(img_, dim)
            cv.imwrite(os.path.join(resize, "resize%d.jpg" %dem),resized)
            dem = dem + 1               
    else:
        b = None
        print("Tạm biệt")
                                       
            
            
                
                    
            
            
        
            
        
