from flask import Flask, session, redirect, url_for, request, render_template
import os 
from random import randint
from sql import get_question, get_quizes

def choose_quiz():
    if request.method == 'GET':
        quizes = get_quizes()
        return render_template('web_html.html', quizes=quizes)
    else:
        peremennay = request.form.get('quizes')
        session['quiz'] = peremennay
        session['question'] = 0
        return redirect(url_for('test'))
    

def test():
    result = get_question(session['question'], session['quiz'])
    if result is None or len(result) == 0:
        redirect(url_for('results'))
    else:
        session['question'] = result[0]
    return f'<h1>{str(result)}</h1>1'

def results():
    pass
folder = os.getcwd()

app = Flask(__name__, template_folder=folder, static_folder=folder)
app.config['SECRET_KEY'] = 'password'
app.add_url_rule('/', 'choose_quiz', choose_quiz, methods = ['post', 'get'])
app.add_url_rule('/test', 'test', test, methods = ['post', 'get'])
app.add_url_rule('/results', 'results', results, methods = ['post', 'get'])
app.run()