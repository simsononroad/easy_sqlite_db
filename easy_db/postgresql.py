class postgresql:
    def __init__(self, username: str, password: str, host: str, db_name: str, port=5432):
        self.username = username
        self.password = password
        self.host = host
        self.db_name = db_name
        self.port = port
    