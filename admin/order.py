from flask import make_response, session
from datetime import datetime, timedelta
import json
from flask_jwt_extended import jwt_required

from . import admin
from model.db import Mydb
from flask import session

@jwt_required()
@admin.route("/order/<int:order_id>")
def get_order_by_id(order_id):
    pass

@jwt_required()
@admin.route("/orders")
def get_orders():
    pass

@jwt_required()
@admin.route("/orders/start=<start_date_string>&end=<end_date_string>")
def get_orders_by_date(start_date_string, end_date_string):
    pass