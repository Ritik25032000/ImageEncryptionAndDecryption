from tkinter import *
from tkinter import messagebox
from VTTV import text_voice as v
from SendMail import Email_Sent as es
from subprocess import call
import os


def clear():
    my_text.delete(1.0, END)

def get_text():
    text=my_text.get(1.0,21.0)
    es.feedback(text)
    root.destroy()
    call(["python","Main.py"])

def Exit():
    messagebox.showinfo("","Exiting")
    root.destroy()

def back():
    root.destroy()
    call(["python","Main.py"])


os.system("mode con cols=50")
os.system("mode con lines=20")
root = Tk()
root.title('Feedback Form')
root.geometry("800x650+100+30")
    
my_text = Text(root, width=50, height=20, font=("Helvetica", 15))
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear Screen", command=clear)
clear_button.grid(row=0, column=0)

get_text_button = Button(button_frame, text="Submit here", command=get_text)
get_text_button.grid(row=0, column=1, padx=20)

Button(root, text="Exit", command=Exit ,height = 1, width = 10).place(x=400, y=550)
Button(root, text="back", command=back ,height = 1, width = 10).place(x=300, y=550)

root.mainloop()
