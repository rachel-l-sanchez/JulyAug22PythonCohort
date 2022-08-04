from flask_app.controllers import dojosNinjas
from flask_app.models import ninja, dojo
from flask_app import app

if __name__ =="__main__":
    app.run(debug=True, port = 5001)