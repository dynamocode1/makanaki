from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

from . import views
from . import auth
import cloudinary
import cloudinary.uploader
import cloudinary.api