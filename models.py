from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return 'User %r' % self.fullname

    def serialize(self):
        return{
            'id': self.id,
            'fullname': self.fullname,
            'email': self.email
        }

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(50), nullable=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    #user = db.relationship(User, backref=backref('children', cascade='all, delete'))

    def __repr__(self):
        return 'Score %r' % self.content

    def serialize(self):
        return{
            'id': self.id,
            'content': self.content,
            'user':self.user,
            'image':self.image
            #'user': self.user.serialize()
        }