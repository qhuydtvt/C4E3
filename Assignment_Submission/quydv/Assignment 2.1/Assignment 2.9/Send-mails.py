import xlrd
import smtplib

email_list_file_location = "/Users/DvQ/Desktop/C4E/email-list-test.xlsx"
email_list_workbook = xlrd.open_workbook(email_list_file_location) #code co chay nhung khong mo dc file?
email_list_sheet = email_list_workbook.sheet_by_index(0)
prinskyengmail = email_list_sheet.cell_value(0,1)
prinskyenyahoo = email_list_sheet.cell_value(1,1)
quydinh3195 = email_list_sheet.cell_value(2,1)

email_list = []
email_list.append(prinskyengmail)
email_list.append(prinskyenyahoo)
email_list.append(quydinh3195)
    
user_name = "c4e3.techkids"
password = "xanhgimaxanhthe"

for email in email_list:
    from_addr = "c4e3.techkids@gmail.com"
    to_addr = email
    msg = "Subject: Quy oi\nQuy dep trai vai"
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo() #chao Gmail
    server.starttls() #thiet lap mot duong truyen bao mat voi Gmail
    server.login(user_name, password)
    server.sendmail(from_addr, to_addr, msg)

server.close()
