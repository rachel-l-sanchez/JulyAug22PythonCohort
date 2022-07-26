from flask import Flask, render_template
app=Flask(__name__,template_folder='templates')

color_wheel = {
        'blue': '#0000FF',
        'coral':'#FF7F50',
        'rebeccapurple':'#663399',
        'orange':'#FFA500',
        'yellow':'#FFFF00',
        'green':'#008000',
        'black':'#000000',
        'pink':'#FFC0CB',
        'red': '#FF0000',
        'beige': '#FFEFD5',
    }
  
@app.route('/')
def default():
    return render_template('index.html', x=int(4), y=int(4), color='red', opposite_color = 'coral')

@app.route('/4')
def small_check():
    return render_template('index.html', x=int(4),y = int(8), color='green', opposite_color='beige')

@app.route('/<int:x>/<int:y>/<color>/<opposite_color>')
def assigned_val(x,y, color, opposite_color):
    return render_template('index.html',x = int(x), y=int(y), color=color, opposite_color = opposite_color)

if __name__ =='__main__':
    app.run(debug=True)