# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 10:56:31 2021

@author: DELL
"""

import speech_recognition as sr

import tkinter as tk
from tkinter import * 
'''
hueanh=tk.Tk() #tao cua so
hueanh.geometry('500x500')
hueanh.title('Text!')
hueanh.configure(background='gray')

heading = Label(hueanh,text="hello")
'''
def start():
    #Khởi tạo Recognizer
    phanAnh07 = sr.Recognizer()
    with sr.Microphone() as source:
        # Xử lí nhận diện
         phanAnh07.adjust_for_ambient_noise(source, duration=1)
         print("Mời bạn nói...")
         # đọc âm thanh từ mic
         audio_data = phanAnh07.record(source, duration=15)
         print("Bạn đang nói...")
         try:
             # Chuyển gióng nói thành văn bản
             text = phanAnh07.recognize_google(audio_data,language="vi")
         except:
             text = "bạn nói gì mình không hiểu!" 
         print("Bạn đã nói là: {}".format(text))
'''
upload= Button(hueanh,text="Bắt đầu",
               command = start, padx=10,pady=5)
upload.pack(side=TOP,pady=50)


hueanh.mainloop()

'''
start()