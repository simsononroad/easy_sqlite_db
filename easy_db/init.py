import sqlite3

db_name_n = ""


def init_db(db_name):

    global db_name_n
    con = sqlite3.connect(f"{db_name}")
    cur = con.cursor()
    db_name_n = db_name
    
    print("Adatbázis létrehozva!")
    return db_name_n

def create_table(table_name, coloumns):
    print(db_name_n)
    con = sqlite3.connect(db_name_n)
    cur = con.cursor()
    coloumn = ""
    for col in coloumns:
        coloumn += f"{col}, "
    coloumn += "id"
    print(coloumn)
    try:
        cur.execute(f"CREATE TABLE {table_name}(id INTEGER AUTOINCREMENT, a)")
        print("Tábla létrehozva")
    except:
        pass

def add_element(table_name, column_name, content):
    print(db_name_n)
    con = sqlite3.connect(db_name_n)
    cur = con.cursor()
    ins = cur.execute(f"insert into {table_name} ({column_name}) values ('{content}')")
    con.commit()
    print(f"{content} behelyezve ide: {column_name}")