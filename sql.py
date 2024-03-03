import sqlite3
cursor = None
con = None
name = 'name.sqlite' 

def set_con():
    global cursor, con
    con = sqlite3.connect(name)
    cursor = con.cursor()

def del_con():
    cursor.close()
    con.close()

def make_select(text):
    cursor.execute(text)
    con.commit()

def create_tables():
    set_con()
    cursor.execute('PRAGMA foreign_keys=on')
    make_select('''CREATE TABLE quiz(
        id INTEGER PRIMARY KEY,
        name VARCHAR
    )''')
    make_select('''CREATE TABLE questions(
        id INTEGER PRIMARY KEY,
        question VARCHAR,
        anser VARCHAR,
        wrong_1 VARCHAR,
        wrong_2 VARCHAR,
        wrong_3 VARCHAR
    )''')
    make_select('''CREATE TABLE connection(
        id INTEGER PRIMARY KEY,
        id_quiz INTEGER,
        id_question INTEGER,
        FOREIGN KEY(id_quiz) REFERENCES quiz(id),
        FOREIGN KEY(id_question) REFERENCES questions(id)
    )''')
    del_con()