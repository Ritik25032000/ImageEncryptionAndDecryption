from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from subprocess import call
from SendMail import Email_Sent as es
from VTTV import text_voice as v
from data import File_Data as fd
import os

def pass_strength(password):
    c=0
    l=[0,0,0,0]
    for i in password:
        if (i.isdigit()):
            l[3]=l[3]+1
        elif (i.islower()):
            l[0]=l[0]+1
        elif (i.isupper()):
            l[1]=l[1]+1
        else:
            l[2]=l[2]+1
    for i in l:
        if(i==0):
            c+=1
    if len(password)<8:
        c+=1
    return c

def siup():
    
    uname = e1.get()
    password = e2.get()
    cpassword= e3.get()
    femail = e4.get()
    fpass = e5.get()
    temail = e6.get()

    c=pass_strength(password)

    if c>=3:
        messagebox.showinfo("", "Password is weak, you can change the password")
    elif cpassword != password:
        messagebox.showinfo("", "Password not match")
    else:
        str1 = uname+" "+password+" "+cpassword+" "+femail+" "+fpass+" "+temail
        fd.add_data(str1)
        messagebox.showinfo("", "Signup Successful")
        es.signup_successful()
        fd.writeone()
        root.destroy()
        call(["python","Main.py"])

def Exit():
    x=messagebox.askquestion("Form","Are you sure want to Exit")
    if(x=='yes'):
        root.destroy()  

os.system("mode con cols=50")
os.system("mode con lines=20")
root = Tk()
root.title("SignUp")
root.geometry("800x530+100+50")
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\asd\\Desktop\\Python Project Modules\\images\\signup.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

global e1
global e2
global e3
global e4
global e5


fontStyle = tkFont.Font(family="Times New Roman",size=15)
Label(root, text="UserName",font=fontStyle).place(x=10, y=10)
Label(root, text="Password",font=fontStyle).place(x=10, y=50)
Label(root, text="Confirm Password",font=fontStyle).place(x=10, y=90)

Label(root, text="Email from sending mails",font=fontStyle).place(x=10, y=160)
Label(root, text="Password",font=fontStyle).place(x=10, y=210)

Label(root, text="Email to sending mails",font=fontStyle).place(x=10, y=280)


e1 = Entry(root)
e1.place(x=250, y=12,width=200)
 
e2 = Entry(root)
e2.place(x=250, y=52,width=200)
e2.config(show="*")

e3 = Entry(root)
e3.place(x=250, y=94,width=200)
e3.config(show="*")

e4 = Entry(root)
e4.place(x=250, y=164,width=200)
 
e5 = Entry(root)
e5.place(x=250, y=214,width=200)
e5.config(show="*")


e6 = Entry(root)
e6.place(x=250, y=282,width=200)


Button(root, text="Signup", command=siup ,height = 2, width = 12).place(x=200, y=350)
Button(root, text="Exit", command=Exit ,height = 1, width = 8).place(x=212, y=440)
C.pack()
root.mainloop()

