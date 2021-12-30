from flask import jsonify, request
from datetime import datetime, timedelta

from . import api
from models import Orders
from models import Guests
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@api.route("/orders", methods=["POST"])
def create_new_order():
    pass