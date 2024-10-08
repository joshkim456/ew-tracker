import sqlite3

class Database:
    def __init__(self, url):
        self.url = url

        with sqlite3.connect(url) as db:
            cursor = db.cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS ew (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                subject TEXT NOT NULL,
                beak TEXT NOT NULL,
                dueDate TEXT NOT NULL
            );
            """
            cursor.execute(sql)

            sql_insert = """
            INSERT INTO ew (task, subject, beak, dueDate) VALUES (?, ?, ?, ?);
            """
            cursor.execute(sql_insert, ('Task', 'Subject', 'Beak', '28/02/2007',))
            db.commit()


    def get_ews(self):
        with sqlite3.connect(self.url) as db:
            cursor = db.cursor()

            sql_get = """
            SELECT id, task, subject, beak, dueDate FROM ew;
            """
            cursor.execute(sql_get)
            rows = cursor.fetchall()
            db.commit()
            return rows


    def create_ew(self, task, subject, beak, dueDate):
        with sqlite3.connect(self.url) as db:
            cursor = db.cursor()

            sql_insert = """
            INSERT INTO ew (task, subject, beak, dueDate) VALUES (?, ?, ?, ?);
            """
            cursor.execute(sql_insert, (task, subject, beak, dueDate))
            db.commit()
        
    # EXTRA CREDIT
    def get_ew(self, id):
        """
        TO IMPLEMENT
        """
        pass