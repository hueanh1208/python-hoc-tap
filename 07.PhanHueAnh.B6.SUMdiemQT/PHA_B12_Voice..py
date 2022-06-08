# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 21:01:37 2021

@author: Admin
"""
import speech_recognition as sr

import tkinter as tk
from tkinter import * 
import numpy as np

hueanh07=tk.Tk() #tao cua so
hueanh07.geometry('500x500')
hueanh07.title('Text!')
hueanh07.configure(background='gray')

arr = np.array([
    "Vietnammese : vi",
    "English: en",
    "Chinese: zh-cn",
    "Japanese: ja",
    "Korea: ko",
    "Indonesia: id",
    "Russian: ru"
    ])

def render_arr():
    item = ""
    for i in arr:    
        item = item + i + "\n"
    return item


lb = Label(hueanh, text=render_arr())
lb.pack(side=TOP,anchor=NW)


language = Label(hueanh, text="*Language", background='gray')
language.place(x=150, y=120)

# tạo ô input
lan = StringVar()
language_entry = Entry(textvariable = lan, width="30")
language_entry.place(x=150, y=150)


def start():
    # lấy data từ ô input
    lan_info = lan.get()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Xử lí nhận diện
         r.adjust_for_ambient_noise(source, duration=1)
         print("Mời bạn nói...")
           # đọc âm thanh từ mic
         audio_data = r.record(source, duration=5)
         print("Bạn đang nói...")
         try:
             # Chuyển gióng nói thành văn bản
             text = r.recognize_google(audio_data,language=lan_info)
             t = Label(hueanh07, text = text)
             t.place(x= 150, y = 220)
         except:
             text = "bạn nói gì mình không hiểu!" 
         print("Bạn đã nói là: {}".format(text))
         


button= Button(hueanh07,text="Bắt đầu",
               command = start, padx=10,pady=5)
button.place(x=150, y=180)   


hueanh07.mainloop()





















