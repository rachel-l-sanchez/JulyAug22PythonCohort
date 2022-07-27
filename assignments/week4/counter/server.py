from flask import Flask, render_template,request, redirect, session
app=Flask(__name__,template_folder='templates')
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')
   
@app.route('/visits',methods=['POST'])
def visits():
    session["reset"] = request.form["reset"]
    session["counter"] = request.form["clicker"] # setting the session variable for the incrementing counter button 
    session["any_num"] = request.form['any_num']
    session["plus-two"] = request.form['plus-two']
    
    return redirect('/')

@app.route('/count')
def count_visit():
    if not 'counter' in session:
        session['counter'] = 1 
    else:
        session["counter"] += 1 #incrementing the counter 
            
    return render_template('index.html', counter = int(session['counter']))

@app.route('/destroy_session')
def small_check():
    session.clear()		# clears all keys in session
    
    return redirect('/')

@app.route('/plus-two')
def numTwo():
    if not 'counter' in session:
        session['counter'] = 2  # default value 
    else:
        session["counter"] += 2 #incrementing the counter
            
    return render_template('index.html', counter= int(session['counter']))

@app.route('/any_num', methods=['POST'])
def anyNum():
    num_input = request.form["any_num"]
    session["counter"] += int(num_input) #incrementing the counter 
         
    return render_template('index.html', counter=int(session['counter']))

if __name__ =="__main__":
    app.run(debug=True)