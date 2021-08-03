from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from subprocess import call
from data import File_Data as fd
from encrdecr import Intermediate as im
import os
from VTTV import text_voice as v

def clear_text_two():
   entry2.delete(1.0, END)
   
def clear_text_one():
   entry1.delete(1.0, END)

def encrypt():
    file1 = filedialog.askopenfiles(parent=root,mode='r',filetype=[('jpg file','*.jpg'),('all files','.*')])
    if file1 is not None:
         key=entry2.get(1.0,END)
         for i in file1:
            file_name=i.name
            l = file_name.split('/')
            l=l[-1]
            l= l.split('.')
            fname=l[0]
            
            clear_text_two()
            x=im.check_present_Encrypt(fname)
            if x==0:
               im.insertDB_encrypt(fname,key)
               fi=open(file_name,'rb')
               image = fi.read()
               fi.close()
               image = bytearray(image)
               for index,values in enumerate(image):
                  image[index]=values^int(key)
                  key=int(key)+1
                  key=key%255
               fi1 = open(file_name,'wb')
               fi1.write(image)
               fi1.close()
            else:
               str1="Sorry, sir, but ,'{}' is already encrypted".format(fname)
               v.speak(str1)

def decrypt():
    file1 = filedialog.askopenfiles(parent=root,mode='r',filetype=[('jpg file','*.jpg'),('all files','.*')])
    if file1 is not None:
       key=entry1.get(1.0,END)
       for i in file1:
          file_name=i.name
          l = file_name.split('/')
          l=l[-1]
          l= l.split('.')
          fname=l[0]
        
          clear_text_one()
          x=im.check_present_Encrypt(fname)

          if x!=0:
             im.insertDB_decrypt(fname,key)
             fi=open(file_name,'rb')
             image = fi.read()
             fi.close()
             image = bytearray(image)
             for index,values in enumerate(image):
                image[index]=values^int(key)
                key=int(key)+1
                key=key%255
             fi1 = open(file_name,'wb')
             fi1.write(image)
             fi1.close()
          else:
             str1="Sorry, sir, but ,'{}' is not encrypted".format(fname)
             v.speak(str1)
             

def onClick4():
    root.destroy()
    call(["python","feedback.py"])

def Exit():
    x=messagebox.askquestion("Form","Are you sure want to Exit")
    if(x=='yes'):
        root.destroy()

def moreDetails():
    root.destroy()
    call(["python","frontpartED.py"])

os.system("mode con cols=50")
os.system("mode con lines=20")
root = Tk()
root.title("Main")
root.geometry("800x600+100+50")
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\asd\\Desktop\\Python Project Modules\\images\\encryption.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)        

Button(root,width=10,text="encrypt",command=encrypt).place(x=78,y=200)
Button(root,width=10,text="decrypt",command=decrypt).place(x=78,y=400)
Button(root,bg='yellow',fg='black', text="Feedback", command=onClick4 , height = 1, width = 12).place(x=350, y=550)
Button(root, text="Exit", command=Exit ,height = 1, width = 12).place(x=620, y=550)
Button(root,text="More Details",command=moreDetails).place(x=78,y=550)

entry1 = Text(root,height=1,width=20)
entry1.place(x=40,y=350)

entry2 = Text(root,height=1,width=20)
entry2.place(x=40,y=150)

C.pack()
root.mainloop()


