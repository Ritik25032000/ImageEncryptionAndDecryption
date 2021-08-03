from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from subprocess import call
from encrdecr import Intermediate as im
from SendMail import Email_Sent as es
from data import File_Data as fd
import os

def clear_text_two():
   e2.delete(0, END)
   
def clear_text_one():
   e1.delete(0, END)

def onClick1():
    fname=e1.get()
    clear_text_one()
    str1=im.retKey(fname)
    fd.write_info(str1)
    root.destroy()
    call(["python","shortinfo.py"])
    #print(str1)


def onClick2():
    key=e2.get()
    clear_text_two()
    str1=im.retfilename(key)
    fd.write_info(str1)
    root.destroy()
    call(["python","shortinfo.py"])
    #print(str1)

def onClick3():
    str1=im.completeEncryptreturn()
    es.getEncryptedData(str1)
    
def onClick4():
    str1=im.completeDecryptreturn()
    es.getDecryptedData(str1)
    
def onClick5():
    root.destroy()
    call(["python","Main.py"])
    
def onClick6():
    x=messagebox.askquestion("Form","Are you sure want to Exit")
    if(x=='yes'):
        root.destroy()

os.system("mode con cols=50")
os.system("mode con lines=20")

root = Tk()
root.title("More Details")
root.geometry("800x600+100+50")
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\asd\\Desktop\\Python Project Modules\\images\\frontPartED.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

global e1
global e2
 
Label(root,bg='old lace', text="If you want key and you know filename").place(x=18, y=107)
Label(root,bg='old lace', text="If you want filename and you know key").place(x=18, y=218)
 
e1 = Entry(root,bg="lemon chiffon")
e1.place(x=290, y=107)
 
e2 = Entry(root,bg="lemon chiffon")
e2.place(x=290, y=221)


Button(root,bg='gold',text="Click here",command=onClick1).place(x=480,y=107)
Button(root,bg='gold',text="Click here",command=onClick2).place(x=480,y=219)
Button(root,bg='gold',text="Encrypted Files Details",command=onClick3).place(x=150,y=400)
Button(root,bg='gold',text="Decrypted Files Details",command=onClick4).place(x=500,y=400)
Button(root,bg='gold',width=8,text="back",command=onClick5).place(x=280,y=500)
Button(root,bg='gold',width=8,text="Exit",command=onClick6).place(x=400,y=500)

C.pack()
root.mainloop()
