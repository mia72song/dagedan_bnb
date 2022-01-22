from flask import Blueprint

api = Blueprint("api", __name__)

from . import order, room, add_on_services, email