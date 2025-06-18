import sqlite3


def create_users_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, email TEXT, password TEXT)"""
    )
    conn.commit()
    conn.close()


def create_journal_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS journal (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, entry TEXT, created_at TEXT, sentiment TEXT, emotion TEXT)"""
    )
    conn.commit()


def add_user(first_name, last_name, email, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO user (first_name, last_name, email, password) VALUES (?, ?, ?, ?)""",
        (first_name, last_name, email, password),
    )
    conn.commit()
    conn.close()


def add_journal_entry(user_id: int, entry: str, sentiment: str, emotion: str):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = f"""INSERT INTO journal (user_id, entry, sentiment, emotion) VALUES ('{user_id}', '{entry}', '{sentiment}', '{emotion}')"""
    cursor.execute(query)
    conn.commit()
    conn.close()
