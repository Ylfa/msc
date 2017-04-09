# Þetta les excel skjal og færir gögnin yfir í gagnagrunn

## Skoða næsta skref - Flask

####################### EXCEL #################################
from openpyxl import load_workbook, worksheet
# from openpyxl.styles import Font #sjá bold=True

####################### SQLITE  ################################
import sqlite3 as lite
import sys
con = lite.connect('gogn.db')
cur = con.cursor()


def init_tables():
    print("Database start")
    with con:
        cur.execute('''DROP TABLE IF EXISTS FARM_NAMES''')
        cur.execute('''DROP TABLE IF EXISTS FARM_FAMILY''')
        cur.execute('''DROP TABLE IF EXISTS AREA_ID''')
        cur.execute('''CREATE TABLE IF NOT EXISTS FARM_FAMILY(
          FAMILY_ID INTEGER PRIMARY KEY AUTOINCREMENT,
          FARM_ID INTEGER,
          FAMILY_YEAR BLOB,
          FAMILY_DATA BLOB);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS FARM_NAMES(
          AREA_ID INTEGER,
          FARM_ID INTEGER primary key autoincrement,
          AREA_NAME TEXT,
          FARM_NAME TEXT,
          YEAR_DATA BLOB,
          NAME_DATA BLOB);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS AREA_ID(
          AREA_ID INTEGER primary key autoincrement,
          AREA_NAME TEXT);''')
    return "Database init done."




def get_family(year_data, name_data):
    """
    Iterate through the list of names in order to group names into familiess.
    :param year_data: Column of year information
    :param name_data: Column under name of farm, with names of persons
    :return: Groupings of families. Store id from farm_names together with groups in db.
    """
    """Popp? count up to next None, Append rows up to None, along with
    corresponding years as one element in new lists

    i = 0
    for n in range(0, len(name_data)):

        if name_data[i]:
            Keep counting
        else
            Write to new lists
    years = year_data
    families = name_data
    """
    return years, families


def get_farm_col(list):
    """
    Takes a list of farms of an area and returns the indexes (col nr) of the farms and their names in tuples
    """
    data_list = []
    for index, elem in enumerate(list):
        data_list.append((index, elem))
    data_list = [data for data in data_list if data[1] not in (' ', '  ', None)]
    return data_list


def main():
    n = 0
    id = 1
    wb = load_workbook(filename='Vinnuskjal1.xlsx')
    ws = wb.worksheets[n]
    sheet_names = wb.get_sheet_names()

    a = init_tables()
    print(a)

    while len(sheet_names) > 1:
        data = [ws.cell(row=1, column=i).value for i in
                range(ws.min_column, ws.max_column + 2)]
        new_list = get_farm_col(data)
        data_cleaned = [item for item in data if item not in (None, ' ', '  ')]
        area_id = ws.title
        with con:
            cur.execute('INSERT INTO AREA_ID (AREA_NAME) VALUES (?)', (sheet_names[0],))

            # Data to be stored in table farm_names:
        while len(data_cleaned) > 0:
            b = new_list[0][0]
            year_blob = [ws.cell(row=i, column=b).value for i in range(2, ws.max_row)]
            name_blob = [ws.cell(row=i, column=b+1).value for i in range(2, ws.max_row)]
            sql_insert = [ws.title, id, data_cleaned[0], str(year_blob), str(name_blob)]

            with con:
                cur.execute('INSERT INTO FARM_NAMES (AREA_NAME, AREA_ID, FARM_NAME, YEAR_DATA, NAME_DATA) VALUES (?, ?, ?,?,?)', sql_insert)
                # con.commit()
            del data_cleaned[0]
            del new_list[0]
        n += 1
        id+=1
        ws = wb.worksheets[n]
        sheet_names.pop(0)

main()

"""
with con:
    cur.execute("SELECT * FROM farm_names")
    rows = cur.fetchall()
    for row in rows:
        print(row)
print("All done!")
con.close()
"""
