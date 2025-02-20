import sqlite3
import inspect
import hashlib

def normal_to_hash(atalakitando, encode="UTF-8"):
    password = atalakitando

    password_hash = hashlib.sha256(password.encode(encode)).hexdigest()
    return password_hash


n_szam = 0
class sqlite:
    version = "EasyDB 1.1"
    creator = "Gyuris Dániel"
    website = ["https://op.gyuris.hu", 
               "https://dani.gyuris.hu"]
    github = "https://github.com/simsononroad"
    
    
    def __init__(self, db_name: str, debug_mode: bool):
        self.db_name = db_name
        self.log = debug_mode
        if self.log:
            print(f"""Courrent version: {sqlite.version}\n
Created by: {sqlite.creator}\n
Websites: 1 {sqlite.website[0]} \n
          2 {sqlite.website[1]}\n
Github: {sqlite.github}""")
        else:
            pass


    def init_db(self):
        con = sqlite3.connect(f"{self.db_name}")
        cur = con.cursor()
        if self.log:
            print("Database created")
        else:
            pass

    def create_table(self, table_name, column_name):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        coloumn = ""
        for col in column_name:
            coloumn += f"{col}, "
        coloumn = coloumn[:-2]
        try:
            cur.execute(f"CREATE TABLE {table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, {coloumn})")
            if self.log:
                print("Table created")
            else:
                pass
        except:
            pass

    def add_element(self, table_name: str, column_name: list, contents: list):
        coloumn = ""
        content = ""
        for col in column_name:
            coloumn += f"{col}, "
        coloumn = coloumn[:-2]

        for cont in contents:
            content += f"'{cont}', "
        content = content[:-2]
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        ins = cur.execute(f"insert into {table_name} ({coloumn}) values ({content})")
        conn.commit()
        if self.log:
            print(f"{content} placed here: {column_name}")
        else:
            pass

    def add_hashed_values(self, table_name: str, column_name: list, contents: list, encode = "UTF-8"):
        coloumn = ""
        content = ""
        for col in column_name:
            coloumn += f"{col}, "
        coloumn = coloumn[:-2]

        for cont in contents:
            cont = normal_to_hash(cont)
            content += f"'{cont}', "
        content = content[:-2]
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        ins = cur.execute(f"insert into {table_name} ({coloumn}) values ({content})")
        con.commit()
    
    class average:
        def __init__(self, db_name, table_name: str, column_name: str):
            self.table_name = table_name
            self.column_name = column_name
            self.db_name = db_name 
        def from_database(self):
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            coloumn = ""
            for col in self.column_name:
                coloumn += f"{col}, "
            coloumn = coloumn[:-2]
            
            ins = cur.execute(f"select {coloumn} FROM {self.table_name}")
            output = cur.fetchall()
            
            output_list = []
            
            osszeadas = int()
            
            try:
                for szamok in output:
                    output_list.append(int(szamok[0]))
            except:
                print(f"Have string in the {coloumn} coloumn")
                exit()
            
            for szamok in output_list:
                osszeadas += szamok

            eredmeny = osszeadas/len(output_list)
            
            return eredmeny
        
        def with_value(self, values: list):
            output_list = []
            
            osszeadas = int()
            
            try:
                for szamok in values:
                    output_list.append(int(szamok))
            except:
                print(f"Have string in the value")
                exit()

            for szamok in output_list:
                osszeadas += szamok

            eredmeny = osszeadas/len(output_list)
            
            return eredmeny
            
    def select_item(self, table_name: str, column_name: list, with_condition: bool, condition=None):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        coloumn = ""
        content = ""
        for col in column_name:
            coloumn += f"{col}, "
        coloumn = coloumn[:-2]
        
        if with_condition:
            if condition == None:
                print("Give a condition")
                exit()
            else:
                ins = cur.execute(f"select {coloumn} FROM {table_name} where {condition}")  
                output = cur.fetchall()
        else:  
            ins = cur.execute(f"select {coloumn} FROM {table_name}")
            output = cur.fetchall()
        return output

    def delete_row(self, table_name: str, condition: str):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        ins = cur.execute(f"DELETE FROM {table_name} WHERE {condition}")
        con.commit()
        if self.log:
            print(f"Element deleted where: {condition}")
        else:
            pass
        
    def update_row(self, table_name: str, column_name: str, new_value: str, condition: str):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        ins = cur.execute(f"UPDATE {table_name} SET {column_name} = '{new_value}' WHERE {condition}")
        con.commit()
        if self.log:
            print(f"Element updated where: {condition} to {new_value}")
        else:
            pass
        
        
    def get_db_info(self, table_name: str, column_name: list):
        global n_szam
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Lekérdezés futtatása
        cursor.execute(f"SELECT * FROM {table_name}")

        self.table = table_name
        # Adatok lekérése
        coloumns_db = cursor.fetchall()
        
        cursor.execute(f"SELECT seq FROM sqlite_sequence")
        rows = cursor.fetchall()
        
        b_row = ""
        num_row = 0
        for row in column_name:
            b_row = row
            id = b_row[1]


        cursor.execute(f"SELECT id FROM {table_name}")
        id = cursor.fetchall()
        for ids in id:
            num_row += 1

        #num of coloumn
        szam = 0
        big_col = ""
        for col in column_name:
            szam += 1
            n_szam += 1
            #print(f"{szam}-dik elem: {col}")
            big_col += f"{col}, "
            b_row = row[szam]
        big_col = big_col[:-2]
        
        

        # Kapcsolat lezárása
        conn.close()
        
        return self.db_name, big_col, num_row, szam+1
    
    def add_variable(self, variable):
            """Eltárolja a változó nevét és értékét az adatbázisban."""
            # Hívó keret vizsgálata
            frame = inspect.currentframe().f_back
            var_name = None

            for name, val in frame.f_locals.items():
                if val is variable:
                    var_name = name
                    break

            if var_name is None:
                raise ValueError("Nem sikerült azonosítani a változó nevét.")

            # Adatbázisba mentés
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute("INSERT INTO variables (name, value) VALUES (?, ?)", (var_name, str(variable)))
            con.commit()
            con.close()

            if self.log:
                print(f"Változó mentve: {var_name} = {variable}")
            else:pass
        

        
        
    
#======templates===========

class templates:
    def __init__(self, db_name: str, debug_mode: bool):
        self.db_name = db_name
        self.log = debug_mode
    
    def login(self):
        a = sqlite(self.db_name, debug_mode=False)
        a.create_table(table_name="login", column_name=["name", "password"])

    def chat(self):
        a = sqlite(self.db_name, debug_mode=False)
        a.create_table(table_name="chat", column_name=["sender", "message", "time"])
    
    def shop(self):
        a = sqlite(self.db_name, debug_mode=False)
        a.create_table(table_name="products", column_name=["name", "price", "discount"])
        a.create_table(table_name="customer", column_name=["name", "password"])
    

#=========console==========

import os
class console:
    def __init__(self, debug_mode: bool):
        self.log = debug_mode
    def start(self):
        try:
            os.system("clear")
        except:
            os.system("clear")
        while True:
            command_line = input(">")
            match command_line:
                case "help":
                    print("segítségek")
                case "create db":
                    db_name = input("Database name >> ")
                    a = sqlite(db_name=db_name, debug_mode=self.log)
                    a.init_db()
                case "add table":
                    table_name = input("Table name >> ")
                    columns = input("column name >> ")
                    a.create_table(table_name=table_name, column_name=columns)
                

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