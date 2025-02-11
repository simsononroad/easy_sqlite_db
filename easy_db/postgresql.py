
import psycopg2



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