import sqlite3

class Safecon:
    def __init__(self):
        self.connection = sqlite3.connect("safeconfig.db")
        self.cursor = self.connection.cursor()

    def create_table_users(self):
        pass
    def create_table_passwords(self):
        pass
    def create_table_activities(self):
        pass
