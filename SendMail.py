from VTTV import text_voice as v
import os
import smtplib 
from email.message import EmailMessage
from data import File_Data as fd
import random

class Email_Sent:
    def sent_mail():
        r = fd.ret_data()
        l =r.split()
        #EMAIL_ADDRESS = os.environ.get('my_mail')
        #EMAIL_PASSWORD = os.environ.get('my_password')
        EMAIL_ADDRESS = l[3]
        EMAIL_PASSWORD = l[4]
        TO_EMAIL = l[5]

        doc = "Thanks and regards\nJarvis Bot"
        msg = EmailMessage()
        msg['Subject'] = "Inappropriate Activity"
        msg['From'] = EMAIL_ADDRESS
        msg['To']=  TO_EMAIL

        str1 = "Hey user, please check your device may be someone try to access your device.\n\n\n"

        msg.set_content(str1+doc)


        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)



    def send_password():
        r = fd.ret_data()
        l =r.split()

        EMAIL_ADDRESS = l[3]
        EMAIL_PASSWORD = l[4]
        TO_EMAIL = l[5]

        doc = "Thanks and regards\nJarvis Bot"
        msg = EmailMessage()
        msg['Subject'] = "Forgot Password"
        msg['From'] = EMAIL_ADDRESS
        msg['To']=TO_EMAIL

        usern = l[0]
        passw = l[1]
        str1 = f"Hey user, Your Encryption and Decryption tool username is {usern} and password is {passw}\n\ntake care and Stay safe\n\n\n"

        msg.set_content(str1+doc)
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)

        

    def signup_successful():
        r = fd.ret_data()
        l =r.split()
       
        EMAIL_ADDRESS = l[3]
        EMAIL_PASSWORD = l[4]
        TO_EMAIL = l[5]

        doc = "Thanks and regards\nJarvis Bot"
        msg = EmailMessage()
        msg['Subject'] = "Signup Successful"
        msg['From'] = EMAIL_ADDRESS
        msg['To']= TO_EMAIL

        usern = l[0]
        passw = l[1]
        str1 = f"Hey {usern}, You have successfully signup, now you can start doing encryption and decryption\nIn case of any query you can click on feedback button and write it on feedback box\n\n\n\n"

        msg.set_content(str1+doc)
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)



    def feedback(str1):
        r = fd.ret_data()
        l =r.split()

        EMAIL_ADDRESS = l[3]
        EMAIL_PASSWORD = l[4]
        TO_EMAIL = l[5]

        doc = "Thanks and regards\n"+l[0]
        msg = EmailMessage()
        msg['Subject'] = "Feeback/Message regarding tool"
        msg['From'] = EMAIL_ADDRESS
        msg['To']= TO_EMAIL

        usern = l[0]
        passw = l[1]
        str1=str1+"\n\n\n"

        msg.set_content(str1+doc)
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)


    def reset_successful():
        r = fd.ret_data()
        l =r.split()
        
        EMAIL_ADDRESS = l[3]
        EMAIL_PASSWORD = l[4]
        TO_EMAIL = l[5]

        doc = "Thanks and regards\nJarvis Bot"
        msg = EmailMessage()
        msg['Subject'] = "Reset Successful"
        msg['From'] = EMAIL_ADDRESS
        msg['To']= TO_EMAIL

        usern = l[0]
        passw = l[1]
        str1 = f"Hey {usern}, Your details have reset successfully\nIn case of any query you can click on feedback button and write it on feedback box\n\n\n\n"

        msg.set_content(str1+doc)
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)


    def getCode():
        num=random.randrange(1000, 9999, 1)

        r = fd.ret_data()
        l =r.split()
        
        EMAIL_ADDRESS = l[3]
        EMAIL_PASSWORD = l[4]
        TO_EMAIL = l[5]

        doc = "Thanks and regards\nJarvis Bot"
        msg = EmailMessage()
        msg['Subject'] = "Reset Successful"
        msg['From'] = EMAIL_ADDRESS
        msg['To']= TO_EMAIL

        usern = l[0]
        passw = l[1]
        str1 = f"Hey {usern}, Your OTP is {num}\nIn case of any query you can click on feedback button and write it on feedback box\n\n\n\n"

        msg.set_content(str1+doc)
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)

        return str(num)

    def getEncryptedData(str1):
        r = fd.ret_data()
        l =r.split()

        EMAIL_ADDRESS = l[3]
        EMAIL_PASSWORD = l[4]
        TO_EMAIL = l[5]

        doc = "\nThanks and regards\n"+"Jarvis Bot"
        msg = EmailMessage()
        msg['Subject'] = "Encrypted Data Record"
        msg['From'] = EMAIL_ADDRESS
        msg['To']= TO_EMAIL

        usern = l[0]
        passw = l[1]
        str1=str1+"\n\n\n"

        msg.set_content(str1+doc)
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
        

    def getDecryptedData(str1):
        r = fd.ret_data()
        l =r.split()

        EMAIL_ADDRESS = l[3]
        EMAIL_PASSWORD = l[4]
        TO_EMAIL = l[5]

        doc = "\nThanks and regards\n"+"Jarvis Bot"
        msg = EmailMessage()
        msg['Subject'] = "Decrypted Data Record"
        msg['From'] = EMAIL_ADDRESS
        msg['To']= TO_EMAIL

        usern = l[0]
        passw = l[1]
        str1=str1+"\n\n\n"

        msg.set_content(str1+doc)
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)        
