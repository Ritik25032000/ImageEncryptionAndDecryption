from tkinter import *
from tkinter import messagebox
from subprocess import call
from VTTV import text_voice as v
import datetime
import sys
from data import File_Data as fd
import os

def onClick1():
    messagebox.showinfo("","Start")
    b=fd.onetime()
    if b==True:
        root.destroy()
        call(["python","login.py"])
    else:
        root.destroy()
        call(["python","signup.py"])
    return True

def onClick2():
    messagebox.showinfo("","Exit")
    root.destroy()
    return True

def onClick3():
    v.speak("Welcome Sir, Please click on start, for file encryption and decryption, and Click on Exit button, for exit")
    return True

def clean():
    fd.writezero()
    fd.refresh_data()


os.system("mode con cols=50")
os.system("mode con lines=20")
root = Tk()
root.title("Start")
root.geometry("900x600+100+50")
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\asd\\Desktop\\Python Project Modules\\images\\gehuE.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

 
Button(root,bg='yellow',fg='black', text="Start", command=onClick1 ,height = 1, width = 12).place(x=370, y=200)
Button(root,bg='yellow',fg='black', text="Exit",  command=onClick2 ,height = 1, width = 12).place(x=370, y=300)
Button(root,bg='yellow',fg='black', text="Help", command=onClick3 , height = 1, width = 12).place(x=370, y=450)
Button(root,bg='yellow',fg='black', text="Refresh", command=clean ,height = 1, width = 12).place(x=370, y=520)
C.pack()
root.mainloop()
























        
