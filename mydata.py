import sqlite3


class Safecon:
    def __init__(self):
        self.connection = sqlite3.connect("safeconfig.db")
        self.cursor = self.connection.cursor()
        self.create_table_users()
        self.create_table_passwords()
        self.create_table_activities()

    def create_table_users(self):
        self.cursor.execute("""CREATE  TABLE IF NOT EXISTS users(
                            user_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_name  TEXT NOT NULL,
                            user_password TEXT NOT NULL)""")
        self.connection.commit()

    def create_table_passwords(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS passwords(
                            password_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                            password_website TEXT,
                            password_link TEXT,
                            password_linked_website TEXT,
                            password_mail TEXT,
                            password_second_mail TEXT,
                            password_username TEXT,
                            password_first_name TEXT,
                            password_last_name TEXT,
                            password_birthdate TEXT,
                            password_phone TEXT,
                            password_password TEXT,
                            password_security_question TEXT,
                            password_answer TEXT,
                            password_main_device TEXT,
                            password_purpose_of_use TEXT,
                            password_note TEXT,
                            user_id INTEGER)""")
        self.connection.commit()

    def create_table_activities(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS activities(
                            activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            activity_name TEXT NOT NULL,
                            activity_date TEXT NOT NULL,
                            activity_hour TEXT NOT NULL,
                            activity_note TEXT,
                            user_name TEXT,
                            user_id INTEGER)""")
        self.connection.commit()

        