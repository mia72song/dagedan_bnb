from flask import Blueprint

admin = Blueprint("admin", __name__)

from . import auth, board, order, views, api