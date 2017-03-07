#Fyrsta tilraun:
#Þetta les excel skjal og færir gögnin yfir í gagnagrunn

##Skoða næsta skref - Flask

####################### EXCEL #################################
from openpyxl import load_workbook, worksheet
#from openpyxl.styles import Font #sjá bold=True
import collections
wb = load_workbook(filename='Vinnuskjal1.xlsx')
n = 0
ws = wb.worksheets[n]
sheet_names = wb.get_sheet_names()

####################### SQLITE  ################################
import sqlite3 as lite
import sys
con = lite.connect('gogn.db')
print("Database opened successfully.")
cur = con.cursor()
db_fields = ['ID', 'AREA_NAME', 'FARM_NAME']
lykill = 0
with con:
    cur.execute('''DROP TABLE IF EXISTS FARM_NAMES''');
    cur.execute('''CREATE TABLE IF NOT EXISTS FARM_NAMES(
        ID INTEGER primary key autoincrement,
        AREA_NAME TEXT,
        FARM_NAME TEXT);''')



#Iterate through sheets and get all farm names per sheet
while len(sheet_names) > 1: #not 0 because last sheet is Spurningar
    title = ws.title
    print(title)  # prints name of sheet
    data = [ws.cell(row=1, column=i).value for i in
            range(ws.min_column, ws.max_column)]  # Gets cell values of first row
    #print(data)
    data_cleaned = [item for item in data if item not in (None, ' ', '  ')] #Remove empty columns
    print(data_cleaned)

    #Data to be stored in table farm_names: (primary key key,per ws.title, a row for each farmname in data_cleaned)
    while len(data_cleaned) > 0:
        data_insert = data_cleaned[0]
        sql_insert = [title, data_insert]
        with con:
            cur.execute('INSERT INTO FARM_NAMES (AREA_NAME, FARM_NAME) VALUES (?,?)', sql_insert)
        del data_cleaned[0]
    n = n+1
    ws = wb.worksheets[n]
    sheet_names.pop(0) #Popping because there was no function to get_max_sheets in file


#data2 = [ws.cell(row=i, column=30).value for i in range(1,20)]
#print(data2)

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