from flask import session, make_response, jsonify, request

from . import api
from model.db import Mydb

@api.route("/rooms")
def get_all_rooms():
    pass

@api.route("/room/<type>")
def get_room(type):
    pass
