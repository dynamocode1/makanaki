from flask import render_template, redirect, url_for, request, flash,session
from flask_login import login_user,current_user,logout_user
from ..models import *
from . import *
import cloudinary
import cloudinary.uploader
import cloudinary.api
from . import auth
cloudinary.config(
    cloud_name='dvnflgqs2',
    api_key='975551641336967',
    api_secret='l12W5dcvd3JvHDr7Hi-Wyx9Q17c'
)

@admin_bp.route('/create_post',methods = ['GET','POST'])
@auth.admin
def create_post(*args,**kwargs):
	if request.method == 'POST':
		data = request.form 
		title  = data.get('title')
		body = data.get('body')
		image = request.files.get('image')
		result = cloudinary.uploader.upload(image)
		print(result,image,body,title)
		new_post = Posts(title= title,body = body,image = result['secure_url'])
		db.session.add(new_post)
		db.session.commit()
		return f'added suces{title}'
	return render_template('adminBlog.html')
@admin_bp.route('/loginadmin', methods = ['GET','POST'])
def adminLogin():
	if request.method == 'POST':
		data = request.form
		name = data.get('username')
		password = data.get('Password')
		if name == 'makanaki12345':
			if password == '#makanaki12345':
				session['admin'] = name
				return redirect(url_for('admin.create_post'))

			else:
				flash('Wrong Password')
				return redirect(url_for('admin.adminLogin'))

		else:
			flash('Wrong Username')
			return redirect(url_for('admin.adminLogin'))

	return render_template('adminForm.html')