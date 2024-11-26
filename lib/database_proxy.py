import sqlite3
from lib.constants import DATABASE_PATH


class DatabaseProxy:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(DATABASE_PATH)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS score (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL,
                score INTEGER NOT NULL,
                date VARCHAR(255) DEFAULT (STRFTIME('%d/%m/%Y %H:%M', 'now', 'localtime'))
            )
        """)

    def __del__(self) -> None:
        self.conn.close()

    def save(self, score: dict) -> None:
        self.conn.execute("INSERT INTO score (name, score) VALUES (:name, :score)", score)
        self.conn.commit()

    def get(self) -> list:
        return self.conn.execute("SELECT * FROM score ORDER BY score DESC LIMIT 10").fetchall()