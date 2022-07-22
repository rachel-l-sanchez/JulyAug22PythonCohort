from flask import Flask
app= Flask(__name__)

@app.route('/')
def routes():
    return "Hello World"

@app.route('/dojo')
def dojo():
     return "Dojo"
 
@app.route('/say/<string:name>')
def say(name):
    name = name
    return "Hi, " + name + "!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    word = word
    num = 3
    return f"{{word}} * {{int(num)}}"

if __name__=="__main__":
    app.run(debug=True)
    

