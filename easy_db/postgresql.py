import hashlib
import psycopg2
import inspect


def normal_to_hash(atalakitando, encode="UTF-8"):
    password = atalakitando

    password_hash = hashlib.sha256(password.encode(encode)).hexdigest()
    return password_hash
class postgresql:
    def __init__(self, username: str, password: str, host: str, db_name: str, debug_mode: bool, port=5432):
        self.username = username
        self.password = password
        self.host = host
        self.db_name = db_name
        self.port = port
        self.log = debug_mode
        
    def init_db(self):
        conn = psycopg2.connect(
                        database=self.db_name,
                        host=self.host,
                        user=self.username,
                        password=self.password,
                        port=self.port)
        return conn
        
        
    def create_table(self, table_name: str, column_name: dict, id_autoincrement: bool):
        con = postgresql.init_db(self)
        cur = con.cursor()
        a = []
        for elem in column_name:
            datatye = column_name[elem]
            name = elem
            a.append(f"{name} {datatye}")
        coloumn=", ".join(a)
        try:
            if id_autoincrement == True:
                print("This function is courrently not avaiable")
                
                #try:
                #    cur.execute(f"""
                #                create sequence splog_adfarm_seq
                #                start 1
                #                increment 1
                #                NO MAXVALUE
                #                CACHE 1;
                #                ALTER TABLE fact_stock_data_detail_seq
                #                OWNER TO {self.username};""")
                #except:pass
                #cur.execute(f"CREATE TABLE {table_name} (id INT unique not null, {coloumn});")
                #con.commit()
                
            else:    
                cur.execute(f"CREATE TABLE {table_name} ({coloumn});")
                con.commit()
            if self.log:
                print("Table created")
            else:
                pass
        except:
            if self.log:
                print("The table alredy created or something went wrong.")
            else:
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
        conn = postgresql.init_db(self)
        cur = conn.cursor()
        ins = cur.execute(f"insert into {table_name} ({coloumn}) values ({content})")
        conn.commit()
        if self.log:
            print(f"{content} placed here: {column_name}")
        else:
            pass
        
    def add_hashed_values(self, table_name: str, column_name: list, contents: list, encode = "UTF-8"):
        conn = postgresql.init_db(self)
        cur = conn.cursor()
        coloumn = ""
        content = ""
        for col in column_name:
            coloumn += f"{col}, "
        coloumn = coloumn[:-2]

        for cont in contents:
            cont = normal_to_hash(cont)
            content += f"'{cont}', "
        content = content[:-2]
        
        ins = cur.execute(f"INSERT INTO {table_name} ({coloumn}) values ({content})")
        conn.commit()
        
    class average:
        def __init__(self, db_name, table_name: str, column_name: str):
            self.table_name = table_name
            self.column_name = column_name
            self.db_name = db_name 
        def from_database(self):
            con = postgresql.init_db(self)
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
        con = postgresql.init_db(self)
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
        con = postgresql.init_db(self)
        cur = con.cursor()
        ins = cur.execute(f"DELETE FROM {table_name} WHERE {condition}")
        con.commit()
        if self.log:
            print(f"Element deleted where: {condition}")
        else:
            pass
    
    def update_row(self, table_name: str, column_name: str, new_value: str, condition: str):
        con = postgresql.init_db(self)
        cur = con.cursor()
        ins = cur.execute(f"UPDATE {table_name} SET {column_name} = '{new_value}' WHERE {condition}")
        con.commit()
        if self.log:
            print(f"Element updated where: {condition} to {new_value}")
        else:
            pass
    
    
      
    def get_db_info(self, table_name: str, column_name: list):
        print("WORK IN PROGRESS. DO NOT USE!")
        global n_szam
        conn = postgresql.init_db(self)
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
            con = postgresql.init_db(self)
            cur = con.cursor()
            try:
                cur.execute(f"CREATE TABLE variables (name TEXT, value TEXT);")
                con.commit()  
            except:
                pass
            
            
            variable_name = f"'{var_name}'"
            variable_value = f"'{str(variable)}'"
            print(f"{variable_name}, {variable_value}")
            #ins = cur.execute(f"insert into {table_name} ({coloumn}) values ({content})")
            cur.execute(f"INSERT INTO variables (name, value) VALUES ({variable_name}, {variable_value})")
            con.commit()
                
            con.close()

            if self.log:
                print(f"Változó mentve: {var_name} = {variable}")
            else:pass