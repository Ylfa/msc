#Fyrsta tilraun:
#Þetta les excel skjal og færir gögnin yfir í gagnagrunn

from openpyxl import load_workbook, worksheet
#from openpyxl.styles import Font #sjá bold=True
wb = load_workbook(filename='test.xlsx')
ws = wb['Sheet1']

import sqlite3 as lite
#import sys
con = lite.connect('test.db')
cur = con.cursor()
db_fields = ['Id', 'num', 'Idnum']
# test
for row in ws.get_squared_range(ws.min_column, ws.min_row, ws.max_column, ws.max_row):
    placeholders = []
    vals = []

    for cell in row:
        placeholders.append('?')
        vals.append(cell.value)
    sql = 'INSERT INTO tilraun (' + ','.join(db_fields) + ') VALUES (' + ','.join(placeholders[:len(db_fields)]) + ')'
    with con:
        cur.execute(sql, tuple(vals[:len(db_fields)])) #make sure only db_fields number of columns

with con:
    cur.execute("SELECT * FROM tilraun")
    rows = cur.fetchall()
    for row in rows:
        print(row)
print("All done!")

#    data_sql = cur.fetchone()
#    while data_sql:
#        print(data_sql)
#        data_sql = cur.fetchone()
#    else:
    # print("Second done")