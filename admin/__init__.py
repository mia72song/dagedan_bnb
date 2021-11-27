from flask import Blueprint

admin = Blueprint("admin", __name__)

from . import user, room, order, booking_list, guest