import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'shang-tsung-eats-bread'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:hosta2015@localhost/it_case'
    SQLALCHEMY_TRACK_MODIFICATIONS = False