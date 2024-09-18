import sqlite3

class Safecon:
    def __init__(self):
        self.connection = sqlite3.connect("safeconfig.db")
        self.cursor = self.connection.cursor()

    def create_table_users(self):
        self.cursor.execute("""CREATE  TABLE IF NOT EXISTS users(
                            user_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_name  TEXT NOT NULL,
                            user_password TEXT NOT NULL)""")
        self.connection.commit()
        
    def create_table_passwords(self):
        pass
    def create_table_activities(self):
        pass
