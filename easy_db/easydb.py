import sqlite3


class create:
    version = "EasyDB 1.1"
    creator = "Gyuris Dániel"
    
    
    def __init__(self, db_name: str, debug_mode: bool):
        self.db_name = db_name
        self.log = debug_mode


    def init_db(self):
        con = sqlite3.connect(f"{self.db_name}")
        cur = con.cursor()
        if self.log:
            print("Adatbázis létrehozva!")
        else:
            pass

    def create_table(self, table_name, coloumn_name):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        coloumn = ""
        for col in coloumn_name:
            coloumn += f"{col}, "
        coloumn = coloumn[:-2]
        try:
            cur.execute(f"CREATE TABLE {table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, {coloumn})")
            if self.log:
                print("Tábla létrehozva")
            else:
                pass
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
        if self.log:
            print(f"{content} behelyezve ide: {coloumn_name}")
        else:
            pass


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
        
        
    def get_db_info(self, table_name: str, coloumn_name: list):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Lekérdezés futtatása
        cursor.execute(f"SELECT * FROM {table_name}")

        # Adatok lekérése
        coloumns_db = cursor.fetchall()
        
        cursor.execute(f"SELECT seq FROM sqlite_sequence")
        rows = cursor.fetchall()
        
        b_row = ""
        num_row = 0
        for row in coloumn_name:
            b_row = row
            id = b_row[1]


        cursor.execute(f"SELECT id FROM {table_name}")
        id = cursor.fetchall()
        for ids in id:
            num_row += 1

        #num of coloumn
        szam = 0
        big_col = ""
        for col in coloumn_name:
            szam += 1 
            #print(f"{szam}-dik elem: {col}")
            big_col += f"{col}, "
            b_row = row[szam]
        big_col = big_col[:-2]

        # Kapcsolat lezárása
        conn.close()
        
        return self.db_name, big_col, num_row, szam+1
    
    
    
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