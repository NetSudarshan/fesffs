import sqlite3

conn = sqlite3.connect("bots.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS bots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    token TEXT UNIQUE
)
""")
conn.commit()

def add_bot(token):
    try:
        cur.execute("INSERT INTO bots (token) VALUES (?)", (token,))
        conn.commit()
        return True
    except:
        return False

def get_bots():
    cur.execute("SELECT token FROM bots")
    return [x[0] for x in cur.fetchall()]
