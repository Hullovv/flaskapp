from flask import ( Flask, request, session, 
                   make_response, render_template, 
                   url_for, redirect, flash)
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from lib.form_classes import *

from flask_login import current_user, LoginManager, login_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import os

if __name__ != 'app':
    from lib.db_scripts.db import User, create_user

app = Flask(__name__)

db_nm = os.getenv('DATABASE')
db_host = os.getenv('MYSQL_SERVICE_HOST')
db_port = os.getenv('MYSQL_SERVICE_PORT')
db_user = os.getenv('MYSQL_USER')
db_password = os.getenv('MYSQL_USER_PASSWD')
driver = 'mysql+mysqlconnector'

app.config['SECRET_KEY'] = '123123'
app.config['SQLALCHEMY_DATABASE_URI'] = f"{driver}://{db_user}:{db_password}@{db_host}:{db_port}/{db_nm}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
migrate.init_app(app, db)

@app.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated:
        return render_template('index.html', name=current_user.name) 
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        print(user.get_id())
        login_user(user) #, remember=form.remember_me.data
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        username = form.surname.data
        try:
            email = form.email.data
        except:
            flash('email zanyat')
        password = form.password.data
        create_user(name=name, username=username, email=email, password=password)
    return render_template('registration.html', form=form)


@app.route('/user/<id>')
def show_user(id):
    user = User.query.filter_by(id=id).first()
    if user == None:
        return {'message': 'user not found'}
    return render_template('show_user.html', user=user)

@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(err):
    return render_template('500.html'), 500

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

if __name__ == '__main__':
    manager.run()
