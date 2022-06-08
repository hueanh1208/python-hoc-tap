import speech_recognition as sr
import cv2
import os


print("""
      1. HongKong.mp4
      2. Jeju3.MOV
      3. JejuDocNguoc.MOV
      """)
      
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
             text = "không có số thứ tự file bạn nói!" 
         print("Bạn đã nói là: {}".format(text))
    return text

hueanh07=True
while hueanh07 == True:
    # lấy tên file
    text_voice = voice()
    if text_voice == "một":
        tenfile = 'HongKong.mp4'
        hueanh07=False
    if text_voice == "hai":
        tenfile = "Jeju3.MOV"
        hueanh07=False
    if text_voice == "ba":
        tenfile = "JejuDocNguoc.MOV"
        hueanh07=False
    
        
hueanh = int(input("Nhập số lượng frame: "))
filename = input("Nhập tên file hình: ")
folder = input("Nhập tên thư mục: ")


os.makedirs(folder, exist_ok=True) # TẠO THƯ MỤC LƯU (từ thư viện os - của OS MS. Windows)

cap = cv2.VideoCapture(tenfile)

count = 0
while cap.isOpened():
    ret, frame = cap.read()#chụp ra một khung hình: 
                            #khung chụp được lưu vào biến frame; ret = vị trí tiếp theo của Video 
                            #(sau khung hình vừa chụp)
    cv2.imshow('Khung Hinh', frame)
    name = filename + "%d.jpg" %count
    cv2.imwrite(os.path.join(folder,name) ,frame)
    
    count = count + 1
    if cv2.waitKey(10) & count == hueanh:
        break
cap.release()
cv2.destroyAllWindows()



path = folder
list_img = os.listdir(path)
print (list_img)

anh = True

while anh:
    print (""" 
               1. Chuyển ảnh xám
               2. Cắt khung ảnh
               3. Quanhy ảnh
               4. Co dãn hình ảnh
               5. Thoát
           """)
    chon = input("Chọn: ")
    if chon == "1":
        gray = input("Nhập tên thư mục để lưu: ")
        os.makedirs(gray, exist_ok=True)
        dem = 0
        path_gray = gray
        for file in list_img:
            imPath = os.path.join(path,file)
    
            img_gray = cv2.imread(imPath,cv2.IMREAD_GRAYSCALE)
            cv2.imwrite(os.path.join(gray,"gray%d.jpg" %dem) ,img_gray)
            dem = dem + 1
              
    elif chon == "2":
        # cắt ảnh
        h_s = int(input("Nhập chiều cao bắt đầu: "))
        h_e = int(input("Nhập chiều cao kết thúc: "))
        w_s = int(input("Nhập chiều rộng bắt đầu: "))
        w_e = int(input("Nhập chiều rộng kết thúc: "))
                  
        cut = input("Nhập tên thư mục để lưu: ")
        os.makedirs(cut, exist_ok=True)
        dem = 0


        for img in list_img:
            img_cut = os.path.join(path,img)
            print(img_cut)
            r = cv2.imread(img_cut)
            i = r[h_s:h_e, w_s:w_e]
            cv2.imwrite(os.path.join(cut, "cut%d.jpg" %dem), i)
            dem =dem +1
    elif chon == "3":
        do = int(input("Nhập độ xoay: "))
        rota = input("Nhập tên thư mục để lưu: ")
        os.makedirs(rota, exist_ok=True)
        dem = 0
        for img in list_img:
             img_rota = os.path.join(path,img)
             img_ = cv2.imread(img_rota) 
             (h, w, d) = img_.shape 
             center = (w // 2, h // 2) 
             M = cv2.getRotationMatrix2D(center, do, 1.0) 
             rotated = cv2.warpAffine(img_, M, (w, h))
             cv2.imwrite(os.path.join(rota, "rota%d.jpg" %dem), rotated)
             dem = dem + 1
    elif chon == "4":
        resize = input("Nhập tên thư mục để lưu: ")
        size = int(input("Nhập tỉ lệ: :"))
        os.makedirs(resize, exist_ok=True)
        dem =0
        for img in list_img:
            img_re = os.path.join(path,img)
            img_ = cv2.imread(img_re) 
            (h, w, d) = img_.shape 
            r = float(size) / w 
            dim = (size, int(h * r))
            resized = cv2.resize(img_, dim)
            cv2.imwrite(os.path.join(resize, "resize%d.jpg" %dem),resized)
            dem = dem + 1               
    else:
        anh = None
        print("Tạm biệt")
    

    
      
        



