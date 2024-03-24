from flask import Flask, session, redirect, url_for
from random import randint
from sql import get_question

def choose_quiz():
    global num_quiz, num_quest
    num_quiz = randint(1, 3)
    num_quest = 0
    return '<a href="/test">перейти в тест</a>'

def test():
    global num_quest
    result = get_question(num_quest, num_quiz)
    if result is None or len(result) == 0:
        redirect(url_for('results'))
    else:
        num_quest = result[0]
    return f'<h1>{str(result)}</h1>1'

def results():
    pass

app = Flask(__name__)
app.add_url_rule('/', 'choose_quiz', choose_quiz)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/results', 'results', results)
app.run()
