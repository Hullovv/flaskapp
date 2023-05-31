from mysql.connector import connect, Error 
from sqlalchemy import create_engine
from sqlalchemy.types import String, Date, Integer, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
import os

db = os.getenv('DATABASE')
host = os.getenv('DB_HOST')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_USER_PASSWD')
driver = 'mysql+mysqlconnector'

engine = create_engine(f"{driver}://{user}:{password}@{host}:3306/{db}")

try:
    engine.connect()
    print('connect')
except Exception as err:
    print(err)

class User:
    pass
    # __tablename__ = os.getenv('USER_TABLE')
    # user_id = 
    # name: 
    # username:
    # email: Mapped[str]