
import psycopg2



class postgresql:
    def __init__(self, username: str, password: str, host: str, db_name: str, port=5432, debug_mode = False):
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
        
        
    def create_table(self, table_name: str, column_name: list):
        con = postgresql.init_db(self)
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