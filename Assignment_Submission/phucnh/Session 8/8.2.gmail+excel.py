
def excel(duongdan):
    import xlrd

    book = xlrd.open_workbook(duongdan)
    sheet = book.sheet_by_index(0) #or by the index it has in excel's sheet collection
 
    data = [] #make a data store
    for i in range(sheet.nrows):
        data.append(sheet.row_values(i)) #drop all the values in the rows into data
    return data

def gmail(ten,gmail):
    import smtplib

    user_name="c4e3.techkids"
    password="xanhgimaxanhthe"

    from_addr= "phuc1009@gmail.com"
    to_addr=gmail
    msg="Subject: Hi "+ten+" oi. Phuc day\nNho hom nay 6 ruoi bat dau hoc Hen em toi nay,  OIL from TechKids"


    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(user_name,password)
    server.sendmail(from_addr,to_addr,msg)

    server.close()


ds_lop= excel("D:\CODE\C4E3\github\Assignment_Submission\phucnh\Session 8\mail.xlsx")
for hocvien in ds_lop:    
    gmail(hocvien[0],hocvien[1])
