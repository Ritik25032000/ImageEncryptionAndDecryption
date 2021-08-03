from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from subprocess import call
from encrdecr import Intermediate as im
from data import File_Data as fd
import os

"""
def func(str1="Ritik"):
    taxText.set('Ritik')

"""
def onClick5():
    root.destroy()
    call(["python","frontpartED.py"])
    
def onClick6():
    x=messagebox.askquestion("Form","Are you sure want to Exit")
    if(x=='yes'):
        root.destroy()

os.system("mode con cols=50")
os.system("mode con lines=20")

root = Tk()
root.title("Specific Information")
root.geometry("500x450+100+50")

str1=fd.return_info()
Label(root, text="Information",font=("Arial", 20)).place(x=150, y=10)

l=str1.split(' ')
if len(l)>7:
    Label(root, text=str1,font=("Arial", 12)).place(x=10, y=100)
else:
    Label(root, text=str1,font=("Arial", 14)).place(x=190, y=80)

Button(root,bg='gold',width=8,text="back",command=onClick5).place(x=100,y=350)
Button(root,bg='gold',width=8,text="Exit",command=onClick6).place(x=330,y=350)
root.mainloop()
