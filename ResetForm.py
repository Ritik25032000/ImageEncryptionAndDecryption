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

def details():
    
    uname2 = e1.get()
    password2 = e2.get()
    cpassword2= e3.get()
    femail2 = e4.get()
    fpass2 = e5.get()
    temail2 = e6.get()

    str1=fd.ret_data()
    l=str1.split()
    if uname2 != '':
        l[0]=uname2
    if password2 !='':
        l[1]=password2
    if cpassword2 !='':
        l[2]=cpassword2
    if femail2 !='':
        l[3]=femail2
    if fpass2 !='':
        l[4]=fpass2
    if temail2 !='':
        l[5]=temail2
   

    if password2!='':
        c=pass_strength(password2)

        if c>=3:
            messagebox.showinfo("", "Password is weak, you can change the password")
        elif cpassword2 != password2:
            messagebox.showinfo("", "Password not match")
        else:
            str1 = l[0]+" "+l[1]+" "+l[2]+" "+l[3]+" "+l[4]+" "+l[5]
            fd.add_data(str1)
            messagebox.showinfo("", "Reset Successful")
            es.reset_successful()
            fd.writeone()
            root.destroy()
            call(["python","login.py"])
            
    else:   
        str1 = l[0]+" "+l[1]+" "+l[2]+" "+l[3]+" "+l[4]+" "+l[5]
        fd.add_data(str1)
        messagebox.showinfo("", "Reset Successful")
        es.reset_successful()
        fd.writeone()
        root.destroy()
        call(["python","login.py"])

def Exit():
    x=messagebox.askquestion("Form","Are you sure want to Exit")
    if(x=='yes'):
        root.destroy()  


os.system("mode con cols=50")
os.system("mode con lines=20")
root = Tk()
root.title("Reset Form")
root.geometry("900x600+100+50")
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\asd\\Desktop\\Python Project Modules\\images\\resetform.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

global e1
global e2
global e3
global e4
global e5


fontStyle = tkFont.Font(family="Times New Roman",size=15)
Label(root, text="UserName",font=fontStyle).place(x=10, y=70)
Label(root, text="Password",font=fontStyle).place(x=10, y=120)
Label(root, text="Confirm Password",font=fontStyle).place(x=10, y=170)

Label(root, text="Email from sending mails",font=fontStyle).place(x=10, y=250)
Label(root, text="Password",font=fontStyle).place(x=10, y=300)

Label(root, text="Email to sending mails",font=fontStyle).place(x=10, y=380)


e1 = Entry(root)
e1.place(x=250, y=73,width=200)
 
e2 = Entry(root)
e2.place(x=250, y=120,width=200)
e2.config(show="*")

e3 = Entry(root)
e3.place(x=250, y=173,width=200)
e3.config(show="*")

e4 = Entry(root)
e4.place(x=250, y=252,width=200)
 
e5 = Entry(root)
e5.place(x=250, y=300,width=200)
e5.config(show="*")


e6 = Entry(root)
e6.place(x=250, y=382,width=200)


Button(root, text="Submit", command=details ,height = 1, width = 10).place(x=200, y=430)
Button(root, text="Exit", command=Exit ,height = 1, width = 8).place(x=205, y=480)
C.pack()
root.mainloop()
