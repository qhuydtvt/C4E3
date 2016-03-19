import xlrd
xl_workbook = xlrd.open_workbook("C:\\Users\\James\\Desktop\\Python\\email_list.xlsx")
sheet_names = xl_workbook.sheet_names()
print('sheet name',sheet_names)
xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
emcol = xl_sheet.col(2)
fcol = xl_sheet.col(1)
    
    
import smtplib
user_name = "tho.d.nguyen31"
password = "gudluck68"

from_addr = "tho.d.nguyen31@gmail.com"
for i in emcol:
    to_addr = str(i)
    n = 0
    for n in range(18):
        msg = str.format("Subject: Hello \n Hello {0} \n from _Tho",xl_sheet.cell(n,1))
        server = smtplib.SMTP('smtp.gmail.com:587') #server la object, SMTP la class
        server.ehlo()
        server.starttls() #Chuong trinh bao mat de bao ve username va password
        server.login(user_name, password)
        server.sendmail(from_addr,to_addr,msg)
        server.close()
        n += 1
