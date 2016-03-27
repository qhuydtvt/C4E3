import xlrd
book = xlrd.open_workbook('D:\C4E 3_contact list_class attandance.xlsx')
sheet=book.sheet_by_index(0)
k=sheet.nrows
print (sheet.nrows)
print (sheet.ncols)
for row_index in range(sheet.nrows):
 for col_index in range(sheet.ncols):
        print (sheet.cell(row_index,col_index).value)
i=1
while i<k+1:
    
    import smtplib
    user_name="c4e3.techkids"
    password="xanhgimaxanhthe"
    from_addr= "c4e3.techkids@gmail.com"
    to_addr= sheet.cell(i,1).value
           
    msg= str.format('Subject: Hai hello chao ban {0}',sheet.cell(i,0).value)
    msg=msg.encode('utf-8')
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo() 
    server.starttls() 
    server.login(user_name, password)
    server.sendmail(from_addr, to_addr, msg)
    server.close()
    i=i+1


