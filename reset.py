from tkinter import *
from tkinter import messagebox
from subprocess import call
from SendMail import Email_Sent as es
from VTTV import text_voice as v
from data import File_Data as fd
import os

def askCode():
    if askCode.c==0:
        y=es.getCode()
        askCode.c=y

def submit(x=0):
    y=e1.get()
    if x!=y:
        submit.counter+=1
        messagebox.showerror("showerror", "OTP not match")
    if submit.counter==3:
        es.sent_mail()
    if x==y:
        messagebox.showinfo("showinfo", "OTP match successfully")
        root.destroy()
        call(["python","ResetForm.py"])
            

def letsgo():
    submit(askCode.c)

os.system("mode con cols=50")
os.system("mode con lines=20")
root = Tk()
root.title("Reset Details")
root.geometry("400x300+100+50")
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\asd\\Desktop\\Python Project Modules\\images\\reset.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

global e1
Label(root, text="Enter Code").place(x=10, y=10)

e1 = Entry(root)
e1.place(x=140, y=10)

submit.counter=0
askCode.c=0

Button(root, text="Get OTP", command=askCode ,height = 1, width = 8).place(x=50, y=100)
Button(root, text="Submit", command=letsgo ,height = 1, width = 8).place(x=270, y=100)


C.pack()
root.mainloop()
