from mysql.connector import connect, Error 
from sqlalchemy import create_engine, Column, Table, MetaData, insert, select
from sqlalchemy.types import String, Date, Integer, Float, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
import sqlalchemy as sql
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

from app import db, login_manager

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(100), nullable=False)
    username = db.Column(String(100), nullable=False)
    email = db.Column(String(255), unique=True, nullable=False)
    password = db.Column(String(255), nullable=False) 
    created_at = db.Column(Date, nullable=False, default=datetime.now())

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
def create_user(name, username, email, password):

    new_user = User(
        name = name,
        username = username,
        email = email,
        password = generate_password_hash(password)
    )

    db.session.add(new_user)
    db.session.commit()
    

db.create_all()