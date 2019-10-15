import sqlite3  
  
conn = sqlite3.connect('javatpoint.db')  
import xlrd
# import mysql.connector
import datetime
# Open the workbook and define the worksheet
book = xlrd.open_workbook("E:\\sem-7_Rupesh\\Programs\\testing\\Anand1989.xls")
worksheet = book.sheet_by_index(0)

# Establish a MySQL connection
conn = sqlite3.connect('db.sqlite3')
# database = mysql.connector.connect (host="localhost", user = "root", passwd = "", db = "rainfall")

# Get the cursor, which is used to traverse the database, line by line
# cursor = database.cursor()

# Create the INSERT INTO sql query


# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
# for x in range(total_rows):
#     for y in range(total_cols):
#         record.append(worksheet.cell(x,y).value)
#     table.append(record)
#     record = []
#     x +=1
total_rows = worksheet.nrows
total_cols = worksheet.ncols
for r in range(1, worksheet.nrows):
    DATE      = worksheet.cell(r,0).value
    ET        = worksheet.cell(r,1).value
    EP        = worksheet.cell(r,2).value
    BSS       = worksheet.cell(r,3).value
    RF        = worksheet.cell(r,4).value
    WD        = worksheet.cell(r,5).value
    WD1       = worksheet.cell(r,6).value
    WS        = worksheet.cell(r,7).value
    DT1       = worksheet.cell(r,8).value
    WT1       = worksheet.cell(r,9).value
    DT2       = worksheet.cell(r,10).value
    WT2       = worksheet.cell(r,11).value
    MAXT      = worksheet.cell(r,12).value
    MINT      = worksheet.cell(r,13).value
    RH11      = worksheet.cell(r,14).value
    RH22      = worksheet.cell(r,15).value
    VP11      = worksheet.cell(r,16).value
    VP22      = worksheet.cell(r,17).value
    CLOUDM    = worksheet.cell(r,18).value
    CLOUDE    = worksheet.cell(r,19).value
    SOIL1     = worksheet.cell(r,20).value
    SOIL2     = worksheet.cell(r,21).value
    SOIL3     = worksheet.cell(r,22).value
    SOIL4     = worksheet.cell(r,23).value
    SOIL5     = worksheet.cell(r,24).value
    SOIL6     = worksheet.cell(r,25).value
    MinTtest  = worksheet.cell(r,26).value
    MaxTtest1 = worksheet.cell(r,27).value
    MaxTtest2 = worksheet.cell(r,28).value
    x = xlrd.xldate_as_tuple(DATE, 0)
    x = list(x)
    y = x[0]
    y = str(y)
    z = x[1]
    z = str(z)
    a = x[2]
    a = str(a)
    y = int(y)
    z = int(z)
    a = int(a)
    x = datetime.datetime(y, z, a)
    
    conn.execute("INSERT INTO  weather_data(DATE,ET,EP,BSS,RF,WD,WD1,WS,DT1,WT1,DT2,WT2,MAXT,MINT,RH11,RH22,VP11,VP22,CLOUDM,CLOUDE,SOIL1,SOIL2,SOIL3,SOIL4,SOIL5,SOIL6,MinTtest,MaxTtest1,MaxTtest2)\values(x,ET,EP,BSS,RF,WD,WD1,WS,DT1,WT1,DT2,WT2,MAXT,MINT,RH11,RH22,VP11,VP22,CLOUDM,CLOUDE,SOIL1,SOIL2,SOIL3,SOIL4,SOIL5,SOIL6,MinTtest,MaxTtest1,MaxTtest2)")  
# Close the cursor
conn.close()

# Commit the transaction
conn.commit()

# Close the database connection
conn.close()

# Print results
print("") 
print ("All Done! Bye, for now.")
print ("")
