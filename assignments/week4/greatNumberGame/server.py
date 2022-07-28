from flask import Flask, render_template,request, redirect, session
app=Flask(__name__,template_folder='templates')
app.secret_key = 'keep it secret, keep it safe'

import random

color_wheel = {
        'orange':'#FFA500',
        'yellow':'#FFFF00',
        'green':'#008000',
        'red': '#FF0000'
    }

@app.route('/')
def index():
    number = random.randint(1,101)
    session['num_output'] = number
    session['count'] = 0

    return render_template('number_game.html')

@app.route('/game', methods=['POST'])
def num_game():
    session['guess'] = int(request.form['guess'])
    session['count'] +=1
    
    return redirect('/guess_num')

@app.route('/guess_num')
def guess_num():
    color = 'yellow'
    num = session['num_output']
    if session['count'] > 5:
        lose ='You lose'
        return render_template('number_game.html', lose=lose)
    if session['guess']< num:
        almost_guess = 'Almost, but still too low'
        return render_template('number_game.html', guess=almost_guess, color=color)
    elif session['guess']> num:
        v_close_guess = 'Almost, but still too high'
        return render_template('number_game.html', guess=v_close_guess, color=color) 
    else:
        guessed_it = f"{session['num_output']} was the number and it took {session['count']} guesses"
        color = 'green'
        return render_template('number_game.html', guess=guessed_it, color=color)

@app.route('/you_lose')
def lose():
    if 'count' in session and 'count'== 5: 
        lose = 'You lose'
        return render_template('number_game.html', lose = str(lose))
    return redirect('/')

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True, port=5001)
    
