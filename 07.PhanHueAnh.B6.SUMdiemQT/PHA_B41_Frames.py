# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:45:42 2021

@author: DELL
"""


# B1: NẠP THƯ VIỆN
import cv2 #THƯ VIỆN COMPUTER VISION Version 2 
import os  # THƯ VIỆN OS MS. WINDOWS = Lập thư mục & lưu file khung ảnh (frame)
import numpy as np  #THƯ VIỆN Mummeric Python = LẬP MA TRẬN GIỮ CHỖ ĐỀ GHÉP 2 KHUNG HÌNH (Color và hình lệch Gray)

"""
B2: KHAI BÁO CÁC HẰNG
"""
INPUT_VIDEO = 'HongKong.mp4' # HẰNG = lưu tên Video file Input
OUTPUT_DIR = '07HueAnh'     # HẰNG = Thư mục lưu SUM các Frame hình cắt ra từ Video [trên]

"""
B3: TẠO THƯ MỤC
"""
os.makedirs(OUTPUT_DIR, exist_ok=True) # TẠO THƯ MỤC LƯU (từ thư viện os -của OS MS. Windows)

"""
B4: THỦ TỤC GHÉP Color Frame với Gray Frame (khác biệt) 
"""
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

"""
B5: THỦ TỤC CHÍNH = CẮT VIDEO GỐC [video_path] THÀNH CÁC Frames -> chuyển ảnh xám : GHÉP Color Frame với Gray Frame (khác biệt) 
"""
def main(video_path):
    cap = cv2.VideoCapture(video_path) # PHÁT VIDEO (LẤY video từ CAM thì ghi 0 = không dùng tham số trên)
    last_gray = None # Biến đối tượng hình Gray (so sánh 2 Frames hình được cắt kế liền nhau)
    idx = -1
    while(True):
        ret, frame = cap.read() #Cắt các frame hình: hình color cắt được lưu vào frame, ret = giữ vị trí kế tiếp của video (sau khi cắt) 
        idx += 1
        if not ret: #or cv2.waitKey(10) & 0xFF == ord('q'):  #vị trí kế tiếp ko còn nữa (hết Video)
            print('Dừng đọc Video vì đã hết (%s)' % video_path)
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# convert color image (trong biến đt frame) hình ành xám lưu vào biến đt hình có tên: gray 
        if last_gray is None: # khung hình đầu tiên (last_gray đang None = chưa đc gán lần nào)
            last_gray = gray
            continue         # quay lại vòng while
        diff = cv2.absdiff(gray, last_gray) # frame hình khác biệt giữa hình xám trước(last_gray) và hình gray tiếp theo (gray)
        """
        ghi frame hình ra file = trong TM đã lập ở trên với thủ tục ghép hình: print_image (đã viết ở trên):
            frame: hình color & diff hình lệch của hình xám hiện tại với hình xám kế trước 
        """
        cv2.imwrite(os.path.join(OUTPUT_DIR, 'IMG_%06d.jpg' %idx), print_image(frame, diff)) 
        last_gray = gray # gán frame gray hiện tại => thành gray frane trước -> quay lại while đọc gray frame tiếp
        print('Lưu hình thứ :  @ %d...' % idx)
        pass
    pass
    cap.release() #Giải phóng biến đối tượng Video cap 
    cv2.destroyAllWindows() # Đóng tất cả các cửa số
print('Chạy chương trình với video clip %s' % INPUT_VIDEO)
main(video_path=INPUT_VIDEO)
