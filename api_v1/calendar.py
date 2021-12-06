from flask import session, make_response, jsonify, request

from . import api
from model.db import Mydb

@api.route("/calendar/<start_date>")
def get_seven_days(start_date):
    pass


