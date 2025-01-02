import sqlite3




def init_db(db_name):

    global db_name_n
    con = sqlite3.connect(f"{db_name}")
    cur = con.cursor()

    
    print("Adatbázis létrehozva!")

def create_table(db_name, table_name, coloumns):
    print(db_name)
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    coloumn = ""
    for col in coloumns:
        coloumn += f"{col}, "
    coloumn = coloumn[:-2]
    print(coloumn)
    try:
        cur.execute(f"CREATE TABLE {table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, {coloumn})")
        print("Tábla létrehozva")
    except:
        pass

def add_element(db_name ,table_name, column_name, contents):
    coloumn = ""
    content = ""
    for col in column_name:
        coloumn += f"{col}, "
    coloumn = coloumn[:-2]

    for cont in contents:
        content += f"'{cont}', "
    content = content[:-2]
    print(content)
    print(db_name)
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    ins = cur.execute(f"insert into {table_name} ({coloumn}) values ({content})")
    con.commit()
    print(f"{content} behelyezve ide: {column_name}")

def delete_row(db_name, table_name, condition):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    ins = cur.execute(f"DELETE FROM {table_name} WHERE {condition}")