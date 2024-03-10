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
    
def add_questions():
    set_con()
    list_by_tuple = [
        ('Сколько лет было Пушкину в последний год его жизни?', '37', '47', '29', '36'),
        ('Сколько произведений было написано цикле "Записки охотника"?', '25', '11', '14', '31'),
        ('Кто написал произведение "Тарас-Бульба"?', 'Н.В.Гоголь', 'А.С.Пушкин', 'И.С.Тургенев', 'Автор этого квиза'), 
        ('Сколько всего существует цифр?', '10', '9', 'бесконечное количество', '0'),
        ('Какое число идет после ∞?', '∞', '0', '9999999999999999...', '1')
        ('Какое существует самае маленькое натуральное число?', '10', '1', '0', '-10'),
        ('Чем играют в классический хоккей?', 'шайбой', 'мячом', 'ботинком', 'ничем'),
        ('Сколько по времяни длится матч в "КХЛ" и во многих других лигах мира?', '20 мин', '15 мин', '30 мин', '45 мин'),
        ('')
    ]
    cursor.executemany('''INSERT INTO questions(question, anser, wrong_1, wrong_2, wrong_3)
    VALUES(?, ?, ?, ?, ?)
    ''', list_by_tuple)
    con.commit()
    del_con()

def add_guizes():
    set_con()
    list_by_tuple = [
        ('Тест на знание литературы', 'тест на знание математики', 'тест на знание хоккея', 'тест на знание истории России 19 в.')
    ]