from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user,current_user,logout_user
from ..models import *
from . import auth_bp

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        phone = form.get('phone')
        password = form.get('password')
        confirmed = form.get('confirm-password')
        users = Users.query.filter_by(username=username).first()

        if not users:
            if password == confirmed:
                user = Users(username=username, phone=phone, password=password)
                db.session.add(user)
                db.session.commit()

                login_user(user)

                next_url = request.args.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect(url_for('main.blog', username=username, phone=phone))
            else:
                flash('Password does not match')
                return redirect(url_for('auth.register'))
        else:
            flash('Username has been taken')
            return redirect(url_for('auth.register'))

    return render_template('register.html')
@auth_bp.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        user = Users.query.filter_by(username = username).first()
        if user:
            if password == user.password:
                login_user(user)
                return redirect(url_for('main.blog'))
            else:
                flash('Wrong Password')
                return redirect(url_for('auth.register'))
        else:
            flash('Username Do Not existing')
            return redirect(url_for('auth.register'))

    return render_template('login.html')
@auth_bp.route('/logout')
def logout():
    logout_user()
    # Optionally, you can flash a message or perform other actions before redirecting
    flash('You have been logged out successfully.')
    return redirect(url_for('auth.register'))  # 