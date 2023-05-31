from flask import ( Flask, request, session, 
                   make_response)
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '123123'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

if __name__ == '__main__':
    manager.run()
    #app.run(host="0.0.0.0", port=5000, debug=True)