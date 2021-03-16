from datetime import datetime
from application import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Mentors(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    user = db.relationship('Users', backref='ments')

    def __repr__(self):
        return '{}.{}'.format(self.id, self.last_name)


class Positions(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    position = db.Column(db.String(64), index = True)
    duty = db.Column(db.String(128), index = True)
    user = db.relationship('Users', backref='posit')

    def __repr__(self):
        return '{}.{}'.format(self.id, self.position)


class Stages(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    stage = db.Column(db.String(256))
    description = db.Column(db.Text)
    user = db.relationship('Users', backref='stage')

    def __repr__(self):
        return '{}.{}'.format(self.id, self.stage)


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy=True)
    position_id = db.Column(db.Integer,db.ForeignKey('positions.id'))
    stage_id = db.Column(db.Integer, db.ForeignKey('stages.id'), default=1)
    mentors_id = db.Column(db.Integer, db.ForeignKey('mentors.id'))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    patronym = db.Column(db.String(32))

    def __repr__(self):
        return 'User %r' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return 'Post %r' % self.username



class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id
