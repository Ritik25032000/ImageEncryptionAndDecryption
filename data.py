
class File_Data:

    def writezero():
        f=open("myfile2.txt","w")
        f.write("0")
        f.close()

    def writeone():
        f=open("myfile2.txt","w")
        f.write("1")
        f.close()

    def onetime():
        f=open("myfile2.txt","r")
        r = f.read()
        r = int(r)
        f.close()
        if r==1:
            return True
        else:
            return False

    def add_data(str1):
        f= open("myfile.txt","w")
        f.write(str1)
        f.close()

    
    def ret_data():
        f =open("myfile.txt","r")
        r = f.read()
        f.close()
        return r
    

    def refresh_data():
        f= open("myfile.txt","w")
        f.close()


    def return_info():
        f=open("myfile3.txt","r")
        r=f.read()
        f.close()
        return r

    def write_info(str1):
        f=open("myfile3.txt","w")
        f.write(str1)
        f.close()
