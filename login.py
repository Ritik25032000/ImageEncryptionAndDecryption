from tkinter import *
from tkinter import messagebox
from subprocess import call
from SendMail import Email_Sent as es
from VTTV import text_voice as v
from data import File_Data as fd
import os

def Ok():
    r = fd.ret_data()
    l =r.split()
    Ok.counter+=1
    uname = e1.get()
    password = e2.get()
 
    if(uname == "" and password == ""):
        messagebox.showinfo("", "Blank Not allowed")
        #return False
         
 
    elif(uname == l[0] and password == l[1]):
 
        messagebox.showinfo("","Login Success")
        root.destroy()
        call(["python","Main.py"])
        #return True
        
 
    else :
        messagebox.showinfo("",Ok.counter)
        #return False
        return Ok.counter

def signin():
    c=Ok()
    if(c==2):
        v.speak("Hello Sir, If you forgot, username and password, click on forgot password button")
    if(c==3):
        es.sent_mail()
        root.destroy()

def retPass():
    messagebox.showinfo("","Wait for 5-10 Seconds")
    es.send_password()

def onClick3():
    v.speak("Welcome Sir,  If you forgot, username and password, click on forgot password button")
    
def Exit():
    x=messagebox.askquestion("Form","Are you sure want to Exit")
    if(x=='yes'):
        root.destroy()

def Reset():
    x=messagebox.askquestion("Form","Are you sure want to Reset")
    if(x=='yes'):
        root.destroy()
        call(["python","reset.py"])
    

    
os.system("mode con cols=50")
os.system("mode con lines=20")
root = Tk()
root.title("Login")
root.geometry("900x600+100+50")
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\asd\\Desktop\\Python Project Modules\\images\\signin.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
global e1
global e2
 
Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

Ok.counter=0
 
Button(root, text="Login", command=signin ,height = 1, width = 8).place(x=100, y=100)
Button(root, text="Forgot Password", command=retPass ,height = 1, width = 20).place(x=60, y=180)
Button(root, text="Help", command=onClick3 , height = 1, width = 8).place(x=100, y=260)
Button(root, text="Exit", command=Exit ,height = 1, width = 8).place(x=100, y=340)
Button(root, text="Reset", command=Reset ,height = 1, width = 8).place(x=100, y=420)
C.pack()
root.mainloop()


 
 

        
