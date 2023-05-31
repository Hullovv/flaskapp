from flask import render_template
from app import app

@app.route('/', methods=['GET'])
def show_index():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    pass

@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(err):
    return render_template('500.html'), 500