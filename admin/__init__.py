from flask import Blueprint

admin = Blueprint("admin", __name__)

from . import user, room, order, board, guest, auth
from .auth import login_required