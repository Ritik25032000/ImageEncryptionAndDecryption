from database import database as db
import datetime


class Intermediate:

    #
    def insertDB_encrypt(fname,key):
        x = datetime.datetime.now()
        day=x.strftime("%d")
        month=x.strftime("%m")
        year=x.strftime("%y")
        db.insertion_in_encrypt(fname,key,year,month,day)

    #
    def insertDB_decrypt(fname,key):
        db.delete_in_encrypt(fname,key)
        x = datetime.datetime.now()
        day=x.strftime("%d")
        month=x.strftime("%m")
        year=x.strftime("%y")
        db.insertion_in_decrypt(fname,key,year,month,day)

    #
    def retfilename(key):
        str1=db.ret_from_encrypt_file(key)
        return str1

    #
    def retKey(fname):
        str1=db.ret_from_encrypt_key(fname)
        return str1

    
    def completeEncryptreturn():
        str1=db.ret_from_encrypt_complete()
        return str1

    def completeDecryptreturn():
        str1=db.ret_from_decrypt_complete()
        return str1

    def check_present_Encrypt(fname):
        x=db.check_data_present_encrypt(fname)
        return x
