import sqlite3
import datetime
class DbClient:
    def __init__(self):
        conn = sqlite3.connect("logs.db")
        self.conn = conn
        self.cursor = conn.cursor()
        self.make_db()
    def make_db(self):
        table = """CREATE TABLE IF NOT EXISTS logi_currency(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            rate_date TEXT NOT NULL,
            currency_rate_usd REAL NOT NULL,
            currency_rate_eur REAL NOT NULL,
            jira_ticket TEXT NOT NULL,
            logged_at TEXT NOT NULL
            );
        """
        self.cursor.execute(table)
        self.conn.commit()




    def log_db(self,rate_date,currency_rate_usd,currency_rate_eur,jira_ticket):
        insert_for_db = """INSERT INTO logi_currency(rate_date,currency_rate_usd,currency_rate_eur,jira_ticket,logged_at)
                        VALUES(?,?,?,?,?);"""
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(insert_for_db,(rate_date,currency_rate_usd,currency_rate_eur,jira_ticket,time_now))
        self.conn.commit()
