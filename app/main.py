from flask import Flask, request, session, make_response
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)

@app.route('/', methods=['GET'])
def show_work():
    user_agent = request.headers.get('User-Agent')
    
    return 'hello %s' % user_agent

@app.route('/<name>')
def show_name(name):
    return "Hello %s " % name


@app.route('/123')
def index():
 response = make_response('<h1>This document carries a cookie!</h1>')
 response.set_cookie('answer', '42')
 return response

if __name__ == '__main__':
    manager.run()
    #app.run(host="0.0.0.0", port=5000, debug=True)