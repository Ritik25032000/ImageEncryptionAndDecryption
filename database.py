import mysql.connector


# ecp dcp
class database:

    #
    def insertion_in_encrypt(fname,key,year,mon,day):
        con=mysql.connector.connect(host="localhost",user="root",password="Ritik@98765",database="endetool")
        cur = con.cursor()
        query="Insert into ecp values({},'{}',{},{},{})".format(key,fname,year,mon,day)
        cur.execute(query)
        con.commit()

    #
    def insertion_in_decrypt(fname,key,year,mon,day):
        con=mysql.connector.connect(host="localhost",user="root",password="Ritik@98765",database="endetool")
        cur = con.cursor()
        query="Insert into dcp values({},'{}',{},{},{})".format(key,fname,year,mon,day)
        cur.execute(query)
        con.commit()

    #
    def ret_from_encrypt_key(fname):
        con=mysql.connector.connect(host="localhost",user="root",password="Ritik@98765",database="endetool")
        cur = con.cursor()
        query = "select KeyNo from ecp where Fname='{}'".format(fname)
        cur.execute(query)
        data=cur.fetchall()
        x=cur.rowcount
        str1=""
        if x==0:
            return "There is no file present having name '{}'".format(fname)
        else:
            for i in data:
                str1+=str(i[0])
                str1+="\n"
        return  str1       

    #
    def ret_from_encrypt_file(key):
        con=mysql.connector.connect(host="localhost",user="root",password="Ritik@98765",database="endetool")
        cur = con.cursor()
        query = "select Fname from ecp where KeyNo={}".format(key)
        cur.execute(query)
        data=cur.fetchall()
        x=cur.rowcount
        str1=""
        if x==0:
            return "There is no file present having key ={}".format(key)
        else:
            for i in data:
                str1+=i[0]
                str1+="\n"
        return  str1      

    #
    def ret_from_encrypt_complete():
        con=mysql.connector.connect(host="localhost",user="root",password="Ritik@98765",database="endetool")
        cur = con.cursor()
        query = "select * from ecp"
        cur.execute(query)
        data=cur.fetchall()
        l = ["","Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
        str1 = ""
        if cur.rowcount==0:
            str1="Hey user, this time there is no encrypted image present"
        else:
            for i in data:
                str1+="Key: "+str(i[0])+"\n"+"File Name: "+str(i[1])+"\n"+"Date: "+str(i[4])+":"+l[i[3]]+":"+"20"+str(i[2])+"\n\n"
        return str1
        
        
    #
    def ret_from_decrypt_complete():
        con=mysql.connector.connect(host="localhost",user="root",password="Ritik@98765",database="endetool")
        cur = con.cursor()
        query = "select * from dcp"
        cur.execute(query)
        data=cur.fetchall()
        l = ["","Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
        str1 = ""
        if cur.rowcount==0:
            str1="Sorry, I have no data.."
        else:
            for i in data:
                str1+="Key: "+str(i[0])+"\n"+"File Name: "+str(i[1])+"\n"+"Date: "+str(i[4])+":"+l[i[3]]+":"+"20"+str(i[2])+"\n\n"
        return str1
            
    #
    def delete_in_encrypt(fname,key):
        con=mysql.connector.connect(host="localhost",user="root",password="Ritik@98765",database="endetool")
        cur = con.cursor()
        query = "Delete from ecp where Fname='{}' and KeyNo={}".format(fname,key)
        cur.execute(query)
        con.commit()

    #
    def check_data_present_encrypt(fname):
        con=mysql.connector.connect(host="localhost",user="root",password="Ritik@98765",database="endetool")
        cur = con.cursor()
        query = "select * from ecp where Fname='{}'".format(fname)
        cur.execute(query)
        data=cur.fetchall()
        return cur.rowcount
            
    """
    # If the file is miss or unused or not required
    def permanent_delete_file(fname):
        con=mysql.connector.connect(host="localhost",user="root",password="Ritik@98765",database="endetool")
        cur = con.cursor()
        query1 = "Delete from ecp where Fname=fname"
        query2 = "Delete from dcp where Fname=fname"
        cur.execute(query1)
        cur.execute(query2)
        con.commit()
    """
