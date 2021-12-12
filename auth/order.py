from flask import make_response
from datetime import datetime
import json
from flask_jwt_extended import jwt_required

from . import auth
from model.db import Mydb
from constants import DATE_FORMATTER


@auth.route("/order/<int:order_id>")
@jwt_required()
def get_order_by_id(order_id):
    pass

@auth.route("/orders")
@jwt_required()
def get_orders():
    pass

