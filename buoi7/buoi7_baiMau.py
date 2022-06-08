# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:40:52 2021

@author: DELL
"""
import cv2
import numpy as np
INPUT_IMAGE = "1.jpg" # HẰNG = lưu Hình Input
def apply_sliding_window(img, kernel, padding=0, stride=1): #padding = số pixel mở rộng ảnh input
    #Stride: khoảng cách trượt.
    #kernel: kích thước cửa sổ trượt
    h, w = img.shape[:2] # lấy chiều cao & chiều rộng ảnh 
     
    img_p = np.zeros([h+2*padding, w+2*padding]) # Numpy = lập ma trận trống zero = chiều cao|| rộng + 2 lần pixel mở rộng 
     
    img_p[padding:padding+h, padding:padding+w] = img # gán ảnh vào khung ma trận nêu trên
     
    kernel = np.array(kernel) # lập cửa sổ trượt 
     
    assert len(kernel.shape) == 2 and kernel.shape[0] == kernel.shape[1] 
     # assert =kiểm tra đàm bảo (tương tự if) square kernel = số chiều = 2 và 2 chiều bằng nhau
    assert kernel.shape[0] % 2 != 0 
    # kernel size is odd number = số chiều cao là lè (đương nhiên chiều w cũng lẻ ) = khung vuông 2 chiều có kích thước là số lẻ
    k_size = kernel.shape[0] # chiều cao của khung trượt
    k_half = int(k_size/2) # nửa chiều cao của khung trượt
     
    y_pos = [v for idx, v in enumerate(list(range(k_half, h-k_half))) if idx % stride == 0] # tập vị trí y (dọc)
    x_pos = [v for idx, v in enumerate(list(range(k_half, w-k_half))) if idx % stride == 0] # tập vị trí x (ngang)
     
    new_img = np.zeros([len(y_pos), len(x_pos)]) #lập ma trận khung trồng (chuần bị điền ảnh vào khung trượt) 
    for new_y, y in enumerate(y_pos): #chạy vị trí y trong tập vị trí y đã xác định ở trên
        for new_x, x in enumerate(x_pos): #chạy vị trí x trong tập vị trí x đã xác định ở trên
            if k_half == 0: #bắt đầu điền ảnh từ vị trí 1/2 ảnh đầu (đã xác định ở trên)
                pixel_val = img_p[y, x] * kernel # element-wise multiply = nhân -> mở rộng phần ảnh
            else:
               pixel_val = np.sum(img_p[y-k_half:y-k_half+k_size, x-k_half:x-k_half+k_size] * kernel) 
        # mở rộng = tích vô hướng 2 vector
    new_img[new_y, new_x] = pixel_val 
    # gán vị trí ảnh phù hợp vào vị mới => chuẩn trượt tiếp
    
    return new_img
# HÀM TRƯỢT 3 GAM MÀU = KHÔNG GIAN MÀU RGB
def apply_sliding_window_on_3_channels(img, kernel, padding=0, stride=1): #làm mờ ảnh 
    layer_blue = apply_sliding_window(img[:,:,0], kernel, padding, stride)
    layer_green = apply_sliding_window(img[:,:,1], kernel, padding, stride)
    layer_red = apply_sliding_window(img[:,:,2], kernel, padding, stride)
    
    new_img = np.zeros(list(layer_blue.shape) + [3])
    new_img[:,:,0], new_img[:,:,1], new_img[:,:,2] = layer_blue, layer_green, layer_red
    return new_img
    #GỌI HÀM VỚI THAM SỐ THỰC 
if __name__ == "__main__": 
    img = cv2.imread(INPUT_IMAGE)
    cv2.imshow("Hinh goc",img) 
    new_img = apply_sliding_window_on_3_channels(img, kernel=[[1]], padding=0, stride=2) # làm mở RGB 
    cv2.imshow("Hinh moi",new_img) 
    cv2.imwrite('H_new.jpg', new_img)

 
    print('Kich thuoc hinh GOC:', img.shape) # kích thước hình gốc
    print('Kich thuoc hinh moi:', new_img.shape) #kích thước hình mới sau xử lý 
    print('Luu hinh @ 3DF_new.jpg') # in tên file hình đã lưu
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('------------')
     
    lighten_blur_img = apply_sliding_window_on_3_channels(img, kernel=[[0.33, 0.33, 0.33], [0.33, 0.33, 0.33], [0.33, 0.33, 0.33]], padding=1, stride=1)
     
    cv2.imshow("Hinh lighten_blur",lighten_blur_img)
    
    cv2.imwrite('H_new_blur.jpg', lighten_blur_img)
    
    print('Kích thước hình gốc:', img.shape)
    print('Kích thước sau khi lighten_blur:', lighten_blur_img.shape)
    print('Luu @ 3DF_new_blur.jpg')
    cv2.waitKey(0)
    cv2.destroyAllWindows()