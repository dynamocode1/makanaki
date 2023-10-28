from . import db, login_manager
import time
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(350), unique=True)
    phone = db.Column(db.String(350))
    password = db.Column(db.String(350))
    date = db.Column(db.String(350), default=time.ctime)
    comments = db.Column(db.Integer, db.ForeignKey('comments.id'))
    like = db.Column(db.Integer, db.ForeignKey('likes.id'))


@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    body = db.Column(db.String(81926000))
    image = db.Column(db.String(12345))
    date = db.Column(db.String(1245), default=str(time.ctime()))
    likes = db.relationship('Likes', backref='liked_post')
    comments = db.relationship('Comments', backref='commented_post')
    def add_comments(self,comment):
    	self.comments.append(comment)
    def add_likes(self,like):
    	self.likes.append(like)
    


class Likes(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.Integer, db.ForeignKey('posts.id'))
    date = db.Column(db.String(1245), default=str(time.ctime))
    post = db.Column(db.Integer, db.ForeignKey('posts.id'))
    username = db.Column(db.String(10000))

    likes = db.relationship('Users', backref='user_likes')

class Comments(db.Model):
	__tablename__ = 'comments'
	id = db.Column(db.Integer, primary_key=True)
	post = db.Column(db.Integer, db.ForeignKey('posts.id'))
	text = db.Column(db.String(1245), default=str(time.ctime))
	date = db.Column(db.String(1245), default=str(time.ctime))
	post = db.Column(db.Integer, db.ForeignKey('posts.id'))
	username = db.Column(db.String(10000))
	comments = db.relationship('Users', backref='user_comment')  # Add relationship to comments
    
