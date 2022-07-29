from flask import Flask, render_template,request, redirect, session
app=Flask(__name__,template_folder='templates')
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def create_form():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form.getlist('language')
    session['comment'] = request.form['comment']
    return redirect('/result')
        
@app.route('/result')
def result():

    return render_template('result.html', full_name = session['name'], fave_language = session['language'], cd_location=session['location'],comment = session['comment'])

@app.route('/back')
def back_to_start():
    return redirect('/')

@app.route('/checkbox')
def checkbox():
    checked = request.form.getlist('language')
    print(checked)
    return render_template('result.html', checked=checked)
    
if __name__ =="__main__":
    app.run(debug=True, port = 5001)