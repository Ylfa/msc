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
        cur.execute('''DROP TABLE IF EXISTS FARM_NAMES1''')
        cur.execute('''DROP TABLE IF EXISTS FARM_NAMES2''')
        cur.execute('''DROP TABLE IF EXISTS FARM_NAMES3''')
        cur.execute('''DROP TABLE IF EXISTS FARM_NAMES4''')
        cur.execute('''DROP TABLE IF EXISTS FARM_NAMES5''')
        cur.execute('''DROP TABLE IF EXISTS FARM_NAMES6''')
        cur.execute('''DROP TABLE IF EXISTS FARM_NAMES7''')

        cur.execute('''CREATE TABLE IF NOT EXISTS FARM_FAMILY(
          FAMILY_ID INTEGER PRIMARY KEY AUTOINCREMENT,
          FARM_NAME TEXT,
          FAMILY_YEAR BLOB,
          FAMILY_DATA BLOB);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS FARM_NAMES(
          AREA_ID INTEGER,
          FARM_ID INTEGER primary key autoincrement,
          AREA_NAME TEXT,
          FARM_NAME TEXT,
          YEAR_DATA BLOB,
          NAME_DATA BLOB);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS FARM_NAMES1(
                  AREA_ID INTEGER,
                  FARM_ID INTEGER PRIMARY KEY,
                  AREA_NAME TEXT,
                  FARM_NAME TEXT,
                  YEAR_DATA BLOB,
                  NAME_DATA BLOB);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS FARM_NAMES2(
                          AREA_ID INTEGER,
                          FARM_ID INTEGER PRIMARY KEY,
                          AREA_NAME TEXT,
                          FARM_NAME TEXT,
                          YEAR_DATA BLOB,
                          NAME_DATA BLOB);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS FARM_NAMES3(
                          AREA_ID INTEGER,
                          FARM_ID INTEGER PRIMARY KEY,
                          AREA_NAME TEXT,
                          FARM_NAME TEXT,
                          YEAR_DATA BLOB,
                          NAME_DATA BLOB);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS FARM_NAMES4(
                                  AREA_ID INTEGER,
                                  FARM_ID INTEGER PRIMARY KEY,
                                  AREA_NAME TEXT,
                                  FARM_NAME TEXT,
                                  YEAR_DATA BLOB,
                                  NAME_DATA BLOB);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS FARM_NAMES5(
                          AREA_ID INTEGER,
                          FARM_ID INTEGER PRIMARY KEY,
                          AREA_NAME TEXT,
                          FARM_NAME TEXT,
                          YEAR_DATA BLOB,
                          NAME_DATA BLOB);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS FARM_NAMES6(
                                  AREA_ID INTEGER,
                                  FARM_ID INTEGER PRIMARY KEY,
                                  AREA_NAME TEXT,
                                  FARM_NAME TEXT,
                                  YEAR_DATA BLOB,
                                  NAME_DATA BLOB);''')
        cur.execute('''CREATE TABLE IF NOT EXISTS FARM_NAMES7(
                          AREA_ID INTEGER,
                          FARM_ID INTEGER PRIMARY KEY,
                          AREA_NAME TEXT,
                          FARM_NAME TEXT,
                          YEAR_DATA BLOB,
                          NAME_DATA BLOB);''')

        cur.execute('''CREATE TABLE IF NOT EXISTS AREA_ID(
          AREA_ID INTEGER primary key autoincrement,
          AREA_NAME TEXT);''')
    return "Database init done."


def get_fams(database_row):
    """
    Iterate through the list of names in order to group names into families.
    :param row: One row, one farm containing [farm_name, year_data blob, name_data blob]

    :return: [[farm_name, yr1, fam1],[farm_name, yr2, fam2],[farm_name, yr3, fam3]]
    - Editable web by login: Edit in excel or database?
    """

    """count up to next None, Append rows up to None, along with
    corresponding years as one element in new lists

    i = 0
    for n in range(0, len(name_data)):

        if name_data[i]:
            Keep counting
        else
            Write to new lists
    years = year_data
    families = name_data
    print(blob2[1]) --ger första tecknet, ej första elementet. Hitta str efter , som ej ar None, appenda
    blobs = [blob1, blob2]"""

    return_rows = []
    n = 0
    a = database_row[0]

    b = database_row[1]
    c = database_row[2]

    #testing = []
    #testing.append([a, b[0], c[0]])
    #print(testing[0])



    #print(a)
    #print(c)
    #for i in range(0, len(b)):
    #    print('b'+str(b[i])+'c'+str(c[i]))
    #while len(b)>0:
    d = len(b)
    #print(d)
    for i in range(0, len(b)):
        #print(n)
        if (b[0] in ('', None, ' ','  ')
            and c[0] in ('', None, ' ','  ')
            and n == 0): #báðar fyrstu línur tómar í blobbum, og ekkert fyrir ofan
            del b[0]
            del c[0]
        elif (b[n] in ('', None, ' ','  ')
              and c[n] in ('', None, ' ','  ')
              and n > 0): #báðar tómar, gögn í línum fyrir ofan
            return_rows.append([a, b[:n], c[:n]])
            b = b[n:] #taka út það sem búið er að bæta við sem fjölla
            c = c[n:]
            n = 0 #byrja nýja fjölluskráningu
        else:
            n +=1 #gögn á línunni, halda áfram að skrolla niður


        #return_rows.append([a, b[items 0-counter], c[items 0-counter]])
        #del items 0-counter in list b and c

    return return_rows


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
    area_one = []
    full_list=[]
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
            full_list.append([data_cleaned[0], year_blob, name_blob])
            #while len(year_blob) > 0:
            #    sql_insert = [ws.title, id, data_cleaned[0], year_blob[0], name_blob[0]]
            #print(full_list)
            with con:
                cur.execute('INSERT INTO FARM_NAMES (AREA_NAME, AREA_ID, FARM_NAME, YEAR_DATA, NAME_DATA) VALUES (?,?,?,?,?)', sql_insert)
            #del year_blob[0]
            #del name_blob[0]
            # con.commit()
            del data_cleaned[0]
            del new_list[0]
        n += 1
        id += 1
        ws = wb.worksheets[n]
        sheet_names.pop(0)

    with con:
        cur.execute("SELECT * FROM FARM_NAMES WHERE AREA_ID = 1")
        rows = cur.fetchall()
        for row in rows:
            cur.execute('INSERT INTO FARM_NAMES1 (AREA_ID, FARM_ID, AREA_NAME,  FARM_NAME, YEAR_DATA, NAME_DATA) VALUES (?,?,?,?,?,?)', row)
    with con:
        cur.execute("SELECT * FROM FARM_NAMES WHERE AREA_ID = 2")
        rows = cur.fetchall()
        for row in rows:
            cur.execute('INSERT INTO FARM_NAMES2 (AREA_ID, FARM_ID, AREA_NAME,  FARM_NAME, YEAR_DATA, NAME_DATA) VALUES (?,?,?,?,?,?)', row)
    with con:
        cur.execute("SELECT * FROM FARM_NAMES WHERE AREA_ID = 3")
        rows = cur.fetchall()
        for row in rows:
            cur.execute('INSERT INTO FARM_NAMES3 (AREA_ID, FARM_ID, AREA_NAME,  FARM_NAME, YEAR_DATA, NAME_DATA) VALUES (?,?,?,?,?,?)', row)
    with con:
        cur.execute("SELECT * FROM FARM_NAMES WHERE AREA_ID = 4")
        rows = cur.fetchall()
        for row in rows:
            cur.execute('INSERT INTO FARM_NAMES4 (AREA_ID, FARM_ID, AREA_NAME,  FARM_NAME, YEAR_DATA, NAME_DATA) VALUES (?,?,?,?,?,?)', row)
    with con:
        cur.execute("SELECT * FROM FARM_NAMES WHERE AREA_ID = 5")
        rows = cur.fetchall()
        for row in rows:
            cur.execute('INSERT INTO FARM_NAMES5 (AREA_ID, FARM_ID, AREA_NAME,  FARM_NAME, YEAR_DATA, NAME_DATA) VALUES (?,?,?,?,?,?)', row)
    with con:
        cur.execute("SELECT * FROM FARM_NAMES WHERE AREA_ID = 6")
        rows = cur.fetchall()
        for row in rows:
            cur.execute('INSERT INTO FARM_NAMES6 (AREA_ID, FARM_ID, AREA_NAME,  FARM_NAME, YEAR_DATA, NAME_DATA) VALUES (?,?,?,?,?,?)', row)
    with con:
        cur.execute("SELECT * FROM FARM_NAMES WHERE AREA_ID = 7")
        rows = cur.fetchall()
        for row in rows:
            cur.execute('INSERT INTO FARM_NAMES7 (AREA_ID, FARM_ID, AREA_NAME,  FARM_NAME, YEAR_DATA, NAME_DATA) VALUES (?,?,?,?,?,?)', row)

    """ Hérna kemur fall sem tekur hvern bæ og klippur niður blobba í fjölskyldutímabil.
        full_list= nafn bæjar, ár_blob, nafn_blob
        get_fams: Tekur við bæjarnafn og 2 blobba. Skilar af sér bæjarnafnið og blob-bita flokkaða í tímabil og fjölskyldur
    """
    #print(full_list[0])

        #cur.execute("SELECT * FROM FARM_NAMES1")
        #rows = cur.fetchall()
        #for row in rows:

    #OBS: BREYTA FAM_NAME Í FAM_ID MEÐ ÞVÍ AÐ JOINA VIÐ AÐRA TÖFLU

    #print(full_list[0])
    while len(full_list)>0:
        all_fams = get_fams(full_list[0])

        for i in range(0, len(all_fams)):
            first_fam = [str(all_fams[i][0]), str(all_fams[i][1]), str(all_fams[i][2])]
            with con:
            #sql_insert = [ws.title, id, data_cleaned[0], str(year_blob), str(name_blob)]
                cur.execute('INSERT INTO FARM_FAMILY (FARM_NAME, FAMILY_YEAR, FAMILY_DATA) VALUES (?,?,?)', first_fam)

        del full_list[0]

main()

""""
with con:
    cur.execute("SELECT * FROM FARM_NAMES1")
    rows = cur.fetchall()
    for row in rows:
        print(row)
print("All done!")
con.close()
"""
