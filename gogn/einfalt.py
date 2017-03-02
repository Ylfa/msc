#Fyrsta tilraun:
#Þetta les excel skjal og færir gögnin yfir í gagnagrunn

from openpyxl import load_workbook, worksheet
#from openpyxl.styles import Font #sjá bold=True

wb = load_workbook(filename='Vinnuskjal1.xlsx')
n = 0
ws = wb.worksheets[n]
sheet_names = wb.get_sheet_names()

#Get sheet names
while len(sheet_names) > 1: #not 0 because last sheet is Spurningar
    print(sheet_names.pop(0))

#Get farm_name from a sheet. Save empty cells in order to iterate, or save colnr and only names in order to find what cols to iterate
#print(ws.title) #prints name of sheet

data = [ws.cell(row=1,column=i).value for i in range(ws.min_column,ws.max_column)] #Gets cell values of first row
print(data)


import sqlite3 as lite
import sys
con = lite.connect('gogn.db')
print("Database opened successfully.")
cur = con.cursor()
db_fields = ['ID', 'AREA_NAME', 'FARM_NAME']


#for row in ws.get_squared_range(ws.min_column, ws.min_row, ws.max_column, ws.max_row):
#    placeholders = []
#    vals = []

#    for cell in row:
#        placeholders.append('?')
#        vals.append(cell.value)
#    sql = 'INSERT INTO tilraun (' + ','.join(db_fields) + ') VALUES (' + ','.join(placeholders[:len(db_fields)]) + ')'
#    with con:
#        cur.execute(sql, tuple(vals[:len(db_fields)])) #make sure only db_fields number of columns


with con:
    cur.execute('''CREATE TABLE IF NOT EXISTS FARM_NAMES(
        ID INT PRIMARY KEY,
        AREA_NAME TEXT,
        FARM_NAME TEXT);''')


with con:
    cur.execute("SELECT * FROM farm_names")
    rows = cur.fetchall()
    for row in rows:
        print(row)
print("All done!")
con.close()
#    data_sql = cur.fetchone()
#    while data_sql:
#        print(data_sql)
#        data_sql = cur.fetchone()
#    else:
    # print("Second done")