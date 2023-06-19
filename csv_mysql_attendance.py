import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost',
    user='root',
    password='',
    database='attendance_db'
    )
cursor = mydb.cursor()

with open('Attendance.csv','r+', encoding = "utf_8") as f:
    myDataList = f.readlines()
for row in myDataList:
    entry = row.split(',')
    if len(entry)<2:
        continue
    cursor.execute('INSERT IGNORE INTO attendances(Employee_Name, \
          Time_Check_in, Date_Check_in)' \
          'VALUES(%s, %s, %s)', 
          entry)
#close the connection to the database.
mydb.commit()
cursor.close()
print('done')