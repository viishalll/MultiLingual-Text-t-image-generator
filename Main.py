import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm

import trans as ret
import Driver as genimg

bgcolor="#ffe6e6"
bgcolor1="#e60000"
fgcolor="#660000"


def Home():
        global window
        
        
        def clear():
                
            print("Clear1")
            txt.delete(0, 'end') 
            txt2.delete(0, 'end')
            
        
            

        window = tk.Tk()
        var = IntVar()
        window.title("Image to Text Generation For Local Languages")
        

 
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        

        message1 = tk.Label(window, text="Image to Text Generation For Local Languages" ,bg=bgcolor  ,fg=fgcolor  ,width=70  ,height=2,font=('times', 25, 'italic bold underline')) 
        message1.place(x=50, y=10)

        lbl = tk.Label(window, text="Enter Your Text",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=100, y=100)
        
        txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=400, y=115)

        
       

        lbl2 = tk.Label(window, text="Converted Text",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl2.place(x=100, y=220)

        txt2 = tk.Entry(window, width = 70, bg="white",fg="red",font=('times', 15, ' bold '))
        txt2.place(x=400, y=225)

        

        


        def lan1toeng():
                txt2.delete(0, 'end')
                sym=txt.get()
                if sym !="":
                        translated=ret.get_translation(sym)
                        txt2.insert('end',translated)
                else:
                        tm.showinfo("Input error", "Enter your text")
        def generareimage():
                sym=txt2.get()
                if sym !="":
                        genimg.process(sym)
                else:
                        tm.showinfo("Input error", "Enter your text")



        

        browse = tk.Button(window, text="Translate", command=lan1toeng  ,fg=fgcolor  ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.place(x=650, y=110)
        browse = tk.Button(window, text="Generate Image", command=generareimage  ,fg=fgcolor  ,bg=bgcolor1  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.place(x=350, y=500)


        clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=620, y=500)
         
        

        quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=990, y=500)

        window.mainloop()
Home()
