from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from ..models import *
from . import main_bp
@main_bp.route('/')
def home():
    data = Posts.query.all()
    return render_template('index.html',blogs = data[:3])

@main_bp.route('/blog')
@login_required
def blog():
    blog = Posts.query.all()
    

    return render_template('blog.html',blog_posts = blog)
@main_bp.route('/blog/add_comments/<id>',methods = ['GET','POST'])
@login_required
def add_comment(id):
    data = request.form
    comment_ = data.get('comment')
    blog = Posts.query.filter_by(id = id).first()
    comment = Comments(text = comment_,username = current_user.username)
    comment.comments.append(current_user)
    blog.add_comments(comment)
    db.session.add(comment)
    db.session.add(blog)
    db.session.commit()
    return redirect(url_for('main.blog'))
@main_bp.route('/blog/add_likes/<id>',methods = ['GET','POST'])
@login_required
def add_like(id):
    
    data = request.form
    blog = Posts.query.filter_by(id = id).first()
    like = Likes(username = current_user.username)
    like.likes.append(current_user)
    blog.add_likes(like)
    db.session.add(like)
    db.session.add(blog)
    db.session.commit()
    #print(Posts.query.filter_by(id = id).first().likes[0].likes)

        
    return redirect(url_for('main.blog'))
@main_bp.route('/about')
def about():
    return render_template('about.html')
@main_bp.route('/contact')
def contact():
    return render_template('contact.html')
@main_bp.route('/blog/view/<id>')
@login_required
def view_posts(id):
    post = Posts.query.filter_by(id = id).first()
    comments = post.comments
    likes = post.likes    
    return render_template('readblog.html',blogs = post,comment = comments,like = likes)