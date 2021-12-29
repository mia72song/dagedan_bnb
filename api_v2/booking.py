from flask import jsonify, request
from datetime import datetime, timedelta

from . import api
from models import Bookings
from constants import DATE_FORMATTER

# 初始化response content
body = "" #json
status_code = 0

@api.route("/booking", methods=["POST"])
def create_new_booking():
    pass