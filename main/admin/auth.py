from flask import session , url_for, redirect
from functools import wraps
def admin(view):
	@wraps(view)
	def admin_required(*args,**kwargs):
		if 'admin' in session:
			pass
		else:
			return redirect(url_for('admin.adminLogin'))
		return view(args,kwargs)
	return admin_required