import sqlite3


class create:
    version = "EasyDB 1.0"
    
    def __init__(self, db_name):
        self.db_name = db_name


    def init_db(self):
        con = sqlite3.connect(f"{self.db_name}")
        cur = con.cursor()

        
        print("Adatbázis létrehozva!")

    def create_table(self, table_name, coloumn_name):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        coloumn = ""
        for col in coloumn_name:
            coloumn += f"{col}, "
        coloumn = coloumn[:-2]
        try:
            cur.execute(f"CREATE TABLE {table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, {coloumn})")
            print("Tábla létrehozva")
        except:
            pass

    def add_element(self, table_name: str, coloumn_name: list, contents: list):
        coloumn = ""
        content = ""
        for col in coloumn_name:
            coloumn += f"{col}, "
        coloumn = coloumn[:-2]

        for cont in contents:
            content += f"'{cont}', "
        content = content[:-2]
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        ins = cur.execute(f"insert into {table_name} ({coloumn}) values ({content})")
        con.commit()
        print(f"{content} behelyezve ide: {coloumn_name}")



    def select_item(self, table_name: str, coloumn_name: list):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        coloumn = ""
        content = ""
        for col in coloumn_name:
            coloumn += f"{col}, "
        coloumn = coloumn[:-2]
        ins = cur.execute(f"select {coloumn} FROM {table_name}")
        output = cur.fetchall()
        return output

    def delete_row(self, table_name: str, condition: str):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        ins = cur.execute(f"DELETE FROM {table_name} WHERE {condition}")
        con.commit()
        
    def update_row(self, table_name: str, coloumn_name: str, new_value: str, condition: str):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        ins = cur.execute(f"UPDATE {table_name} SET {coloumn_name} = '{new_value}' WHERE {condition}")
        con.commit()
    
    
#=========dev functions=========

    
def quick_start(coloumn_name: list):
    con = sqlite3.connect(f"database.db")
    cur = con.cursor()
    
    
    coloumn = ""
    for col in coloumn_name:
        coloumn += f"{col}, "
    coloumn = coloumn[:-2]
    try:
        cur.execute(f"CREATE TABLE tables(id INTEGER PRIMARY KEY AUTOINCREMENT, {coloumn})")
        print("Tábla létrehozva")
    except:
        pass
    
    
def quick_add(coloumn_name: list, contents: list):
    coloumn = ""
    content = ""
    
    for col in coloumn_name:
        coloumn += f"{col}, "
    coloumn = coloumn[:-2]
    
    
    for cont in contents:
        content += f"'{cont}', "
    content = content[:-2]
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    ins = cur.execute(f"select {col} FROM tables")
    output = cur.fetchall()
    ins = cur.execute(f"insert into tables ({coloumn}) values ({content})")
    con.commit()
    
def quick_select(coloumn_name: list):
    coloumn = ""
    content = ""
    for col in coloumn_name:
        coloumn += f"{col}, "
    coloumn = coloumn[:-2]
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    ins = cur.execute(f"select {coloumn} FROM tables")
    output = cur.fetchall()
    return output

def quick_delete(condition: str):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    ins = cur.execute(f"DELETE FROM tables WHERE {condition}")
    con.commit()