from flask import ( Flask, request, session, 
                   make_response, render_template )
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from lib.db_scripts import db

class NameForm(FlaskForm):
    name = StringField('Whats your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'GEB1cfikudpLM'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/<name>')
def show_name(name):
    return render_template('user.html', name=name)


@app.route('/', methods=['GET', 'POST'])
def user_login():
    name = ''
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return name, render_template('index.html', form=form, name=name, current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(err):
    return render_template('500.html'), 500

if __name__ == '__main__':
    manager.run()
    #app.run(host="0.0.0.0", port=5000, debug=True)