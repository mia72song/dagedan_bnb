from flask import session, make_response, jsonify

from . import api

@api.route("/user", methods=["POST"])
def login():
    pass

@api.route("/user", methods=["DELETE"])
def logout():
    pass

@api.route("user")
def get_current_user():
    pass