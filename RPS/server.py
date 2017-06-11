from flask import Flask, session, request, redirect, render_template
import random
app=Flask(__name__)
app.secret_key='macbook'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/win')
def win():
    return render_template('win.html', win=session['win'], lose=session['lose'], tie=session['tie'])

@app.route('/lose')
def lose():
    return render_template('lose.html', win=session['win'], lose=session['lose'], tie=session['tie'])

@app.route('/tie')
def tie():
    return render_template('tie.html', win=session['win'], lose=session['lose'], tie=session['tie'])

@app.route('/player2', methods=['POST'])
def player2():
    if 'win' not in session:
        session['win'] = 0
    if 'lose' not in session:
        session['lose'] = 0
    if 'tie' not in session:
        session['tie'] = 0

    if 'rock' in request.form:
        session['clicked'] = 'rock'
    elif 'paper' in request.form:
        session['clicked'] = 'paper'
    else:
        session['clicked'] = 'scissors'

    cpu = random.randrange(1,3)

    if cpu == 1:
        session['cpu'] = 'rock'

    elif cpu == 2:
        session['cpu'] = 'paper'

    else:
        session['cpu'] = 'scissors'

    if session['cpu'] == session['clicked']:
        session['tie'] += 1
        return redirect('/tie')

    elif session['cpu'] == 'rock' and session['clicked'] == 'paper':
        session['win'] += 1
        return redirect('/win')

    elif session['cpu'] == 'rock' and session['clicked'] == 'scissors':
        session['lose'] += 1
        return redirect('/lose')

    elif session['cpu'] == 'paper' and session['clicked'] == 'rock':
        session['lose'] += 1
        return redirect('/lose')

    elif session['cpu'] == 'paper' and session['clicked'] == 'scissors':
        session['win'] += 1
        return redirect('/win')

    elif session['cpu'] == 'scissors' and session['clicked'] == 'rock':
        session['win'] += 1
        return redirect('/win')

    elif session['cpu'] == 'scissors' and session['clicked'] == 'paper':
        session['lose'] += 1
        return redirect('/lose')

@app.route('/reset')
def reset():

    session['win'] = 0

    session['lose'] = 0

    session['tie'] = 0

    return redirect('/')

app.run(debug=True)
