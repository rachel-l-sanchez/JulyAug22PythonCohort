from flask import Flask, render_template
app= Flask(__name__,template_folder='templates')

color = {
        'blue': '#0000FF',
        'coral':'#FF7F50',
        'rebeccapurple':'#663399',
        'orange':'#FFA500',
        'yellow':'#FFFF00',
        'green':'#008000',
        'black':'#000000',
        'pink':'#FFC0CB',
        'red': '#FF0000'
    }
  
@app.route('/')
def default():
    return render_template('playground.html', num=int(4), color='red')

@app.route('/play')
def boxes():
    return render_template('playground.html', num=int(3), color='red')

@app.route('/play/<int:num>')
def num_boxes(num):
    return render_template('playground.html', num=int(num), color='red')

@app.route('/play/<int:num>/<string:color>')
def box_color(num, color):
    return render_template('playground.html',num=int(num), color=color)  

if __name__ =="__main__":
    app.run(debug=True)
    