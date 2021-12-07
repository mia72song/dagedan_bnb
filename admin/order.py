from flask import make_response, session
from datetime import datetime, timedelta
import json
import functools

from . import admin
from model.db import Mydb
from flask import session

def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if session.get("user"):
            result = func(*args, **kwargs)
            return result
    return wrapper

@login_required
@admin.route("/order/<int:order_id>")
def get_order_by_id(order_id):
    pass

@login_required
@admin.route("/orders")
def get_orders():
    pass