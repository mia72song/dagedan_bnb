from flask import Blueprint
from App import csrf

api = Blueprint("api", __name__)

csrf.exempt(api)

from . import room, order, payment, captcha